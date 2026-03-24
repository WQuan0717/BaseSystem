#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Run API tests from OpenAPI specs
"""

import json
import requests
from pathlib import Path
from datetime import datetime


def load_api_spec(spec_file: str = "docs/api_spec.json"):
    """Load API specification"""
    with open(spec_file, "r", encoding="utf-8") as f:
        return json.load(f)


def generate_test_cases(spec: dict):
    """Generate test cases from spec"""
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
    """Run single API test"""
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
            return {"status": "SKIP", "reason": f"Unsupported method: {method}"}

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
    """Run all API tests"""
    print(f"Loading API spec: {spec_file}")
    spec = load_api_spec(spec_file)

    print(f"Generating test cases...")
    test_cases = generate_test_cases(spec)
    print(f"Generated {len(test_cases)} test cases")

    results = []
    passed = 0
    failed = 0
    errors = 0

    print(f"\nStarting tests: {base_url}\n")

    for i, test_case in enumerate(test_cases, 1):
        print(f"[{i}/{len(test_cases)}] Testing {test_case['id']}...")
        result = run_api_test(base_url, test_case)
        results.append({"case": test_case, "result": result})

        if result["status"] == "PASS":
            passed += 1
            print(f"  PASS")
        elif result["status"] == "FAIL":
            failed += 1
            print(f"  FAIL - expected {result.get('expected')}, got {result.get('actual')}")
        else:
            errors += 1
            print(f"  {result['status']} - {result.get('error', '')}")

    report = generate_test_report(results, passed, failed, errors)

    print(f"\nResults: {passed} passed, {failed} failed, {errors} errors")
    print(f"Report saved to: docs/test_api_report.md")

    return report


def generate_test_report(results: list, passed: int, failed: int, errors: int):
    """Generate test report"""
    report_lines = [
        "# API Test Report",
        f"**Test Time**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        f"**Test Environment**: {results[0]['case'].get('base_url', 'N/A') if results else 'N/A'}",
        "",
        "## Summary",
        "",
        f"| Total | Passed | Failed | Errors |",
        f"|-------|--------|--------|--------|",
        f"| {len(results)} | {passed} | {failed} | {errors} |",
        "",
        "## Details",
        ""
    ]

    for item in results:
        test_case = item["case"]
        result = item["result"]

        status_icon = {"PASS": "PASS", "FAIL": "FAIL", "ERROR": "ERROR", "SKIP": "SKIP"}.get(result["status"], "UNKNOWN")

        report_lines.append(f"### {status_icon} {test_case['id']}")
        report_lines.append(f"- **Endpoint**: {test_case['method']} {test_case['path']}")
        report_lines.append(f"- **Description**: {test_case['summary']}")
        report_lines.append(f"- **Status**: {result['status']}")

        if result["status"] == "PASS":
            report_lines.append(f"- **Response Time**: {result.get('time', 'N/A')}s")
        elif result["status"] == "FAIL":
            report_lines.append(f"- **Expected**: {result.get('expected')}")
            report_lines.append(f"- **Actual**: {result.get('actual')}")
        elif result["status"] == "ERROR":
            report_lines.append(f"- **Error**: {result.get('error')}")

        report_lines.append("")

    report_lines.append("---")
    report_lines.append("*Generated by webapp-testing*")

    Path("docs").mkdir(exist_ok=True)
    report_path = "docs/test_api_report.md"
    with open(report_path, "w", encoding="utf-8") as f:
        f.write("\n".join(report_lines))

    return "\n".join(report_lines)


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python run_api_tests.py <base_url> [spec_file]")
        print("Example: python run_api_tests.py http://localhost:8000")
        sys.exit(1)

    base_url = sys.argv[1]
    spec_file = sys.argv[2] if len(sys.argv) > 2 else "docs/api_spec.json"

    run_all_tests(base_url, spec_file)
