#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
运行 API 测试
从 OpenAPI 规格生成并执行 API 测试
"""

import json
import requests
from pathlib import Path
from datetime import datetime


def load_api_spec(spec_file: str = "docs/api_spec.json"):
    """加载 API 规格"""
    with open(spec_file, "r", encoding="utf-8") as f:
        return json.load(f)


def generate_test_cases(spec: dict):
    """生成测试用例"""
    test_cases = []
    
    for path, methods in spec.get("paths", {}).items():
        for method, details in methods.items():
            test_case = {
                "id": f"{method.upper()}_{path.replace('/', '_')}",
                "method": method.upper(),
                "path": path,
                "summary": details.get("summary", ""),
                "parameters": details.get("parameters", []),
                "request_body": details.get("requestBody", {}),
                "responses": details.get("responses", {})
            }
            test_cases.append(test_case)
    
    return test_cases


def run_api_test(base_url: str, test_case: dict):
    """运行单个 API 测试"""
    
    url = f"{base_url}{test_case['path']}"
    method = test_case['method']
    
    try:
        if method == "GET":
            response = requests.get(url)
        elif method == "POST":
            response = requests.post(url, json={})
        elif method == "PUT":
            response = requests.put(url, json={})
        elif method == "DELETE":
            response = requests.delete(url)
        else:
            return {"status": "SKIP", "reason": f"不支持的方法：{method}"}
        
        # 检查响应码
        expected_codes = list(test_case.get("responses", {}).keys())
        if expected_codes:
            expected_code = int(expected_codes[0])
            if response.status_code == expected_code:
                return {
                    "status": "PASS",
                    "code": response.status_code,
                    "time": response.elapsed.total_seconds()
                }
            else:
                return {
                    "status": "FAIL",
                    "expected": expected_code,
                    "actual": response.status_code,
                    "response": response.text[:200]
                }
        else:
            return {
                "status": "PASS" if response.ok else "FAIL",
                "code": response.status_code,
                "time": response.elapsed.total_seconds()
            }
    
    except Exception as e:
        return {"status": "ERROR", "error": str(e)}


def run_all_tests(base_url: str, spec_file: str = "docs/api_spec.json"):
    """运行所有 API 测试"""
    
    print(f"📋 加载 API 规格：{spec_file}")
    spec = load_api_spec(spec_file)
    
    print(f"📝 生成测试用例...")
    test_cases = generate_test_cases(spec)
    print(f"✓ 生成 {len(test_cases)} 个测试用例")
    
    results = []
    passed = 0
    failed = 0
    errors = 0
    
    print(f"\n🚀 开始测试：{base_url}\n")
    
    for i, test_case in enumerate(test_cases, 1):
        print(f"[{i}/{len(test_cases)}] 测试 {test_case['id']}...")
        result = run_api_test(base_url, test_case)
        results.append({"case": test_case, "result": result})
        
        if result["status"] == "PASS":
            passed += 1
            print(f"  ✅ PASS")
        elif result["status"] == "FAIL":
            failed += 1
            print(f"  ❌ FAIL - 期望 {result.get('expected')}, 实际 {result.get('actual')}")
        else:
            errors += 1
            print(f"  ⚠️  {result['status']} - {result.get('error', '')}")
    
    # 生成报告
    report = generate_test_report(results, passed, failed, errors)
    
    print(f"\n{'='*60}")
    print(f"测试结果：{passed} 通过，{failed} 失败，{errors} 错误")
    print(f"测试报告已保存到：docs/test_api_report.md")
    
    return report


def generate_test_report(results: list, passed: int, failed: int, errors: int):
    """生成测试报告"""
    
    report_lines = [
        "# API 测试报告",
        f"**测试时间**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        f"**测试环境**: {results[0]['case'].get('base_url', 'N/A') if results else 'N/A'}",
        "",
        "## 测试概览",
        "",
        f"| 总计 | 通过 | 失败 | 错误 |",
        f"|------|------|------|------|",
        f"| {len(results)} | {passed} | {failed} | {errors} |",
        "",
        "## 测试详情",
        ""
    ]
    
    for item in results:
        test_case = item["case"]
        result = item["result"]
        
        status_icon = {"PASS": "✅", "FAIL": "❌", "ERROR": "⚠️", "SKIP": "⏭️"}.get(result["status"], "❓")
        
        report_lines.append(f"### {status_icon} {test_case['id']}")
        report_lines.append(f"- **接口**: {test_case['method']} {test_case['path']}")
        report_lines.append(f"- **描述**: {test_case['summary']}")
        report_lines.append(f"- **状态**: {result['status']}")
        
        if result["status"] == "PASS":
            report_lines.append(f"- **响应时间**: {result.get('time', 'N/A')}s")
        elif result["status"] == "FAIL":
            report_lines.append(f"- **期望**: {result.get('expected')}")
            report_lines.append(f"- **实际**: {result.get('actual')}")
        elif result["status"] == "ERROR":
            report_lines.append(f"- **错误**: {result.get('error')}")
        
        report_lines.append("")
    
    report_lines.append("---")
    report_lines.append("*报告生成 by se-testing*")
    
    # 保存报告
    Path("docs").mkdir(exist_ok=True)
    report_path = "docs/test_api_report.md"
    with open(report_path, "w", encoding="utf-8") as f:
        f.write("\n".join(report_lines))
    
    return "\n".join(report_lines)


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("用法：python run_api_tests.py <基础 URL> [API 规格文件]")
        print("示例：python run_api_tests.py http://localhost:8000")
        sys.exit(1)
    
    base_url = sys.argv[1]
    spec_file = sys.argv[2] if len(sys.argv) > 2 else "docs/api_spec.json"
    
    run_all_tests(base_url, spec_file)
