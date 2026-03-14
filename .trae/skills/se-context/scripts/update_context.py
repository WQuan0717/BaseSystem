#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
更新项目状态
更新当前阶段、进度和阻塞问题
"""

import json
import os
import shutil
from datetime import datetime
from pathlib import Path


def load_state():
    """加载项目状态"""
    state_path = "docs/context/project_state.json"
    if not os.path.exists(state_path):
        print("❌ 项目状态文件不存在")
        return None
    
    with open(state_path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_state(state):
    """保存项目状态并创建历史备份"""
    state_path = "docs/context/project_state.json"
    
    # 备份当前状态
    if os.path.exists(state_path):
        history_path = f"docs/context/history/state_{datetime.now().strftime('%Y-%m-%d_%H%M%S')}.json"
        shutil.copy2(state_path, history_path)
        print(f"✓ 已备份历史状态：{history_path}")
    
    # 更新最后更新时间
    state["last_updated"] = datetime.now().isoformat()
    
    # 保存新状态
    with open(state_path, "w", encoding="utf-8") as f:
        json.dump(state, f, ensure_ascii=False, indent=2)
    print(f"✓ 已更新项目状态：{state_path}")


def update_phase(state, new_phase):
    """更新阶段"""
    old_phase = state["current_phase"]
    
    if old_phase != "init":
        if old_phase not in state["completed_phases"]:
            state["completed_phases"].append(old_phase)
    
    if new_phase in state["pending_phases"]:
        state["pending_phases"].remove(new_phase)
    
    state["current_phase"] = new_phase
    
    # 计算进度
    total_phases = 6  # requirements, architecture, design, development, testing, documentation
    completed = len(state["completed_phases"])
    state["completion_percentage"] = int((completed / total_phases) * 100)
    
    print(f"✓ 阶段更新：{old_phase} → {new_phase}")
    print(f"✓ 进度：{state['completion_percentage']}%")


def add_blocking_issue(state, description, severity="medium"):
    """添加阻塞问题"""
    issue = {
        "description": description,
        "severity": severity,
        "status": "open",
        "created_at": datetime.now().isoformat()
    }
    state["blocking_issues"].append(issue)
    print(f"✓ 添加阻塞问题：{description}")


def resolve_blocking_issue(state, issue_index):
    """解决阻塞问题"""
    if 0 <= issue_index < len(state["blocking_issues"]):
        state["blocking_issues"][issue_index]["status"] = "resolved"
        state["blocking_issues"][issue_index]["resolved_at"] = datetime.now().isoformat()
        print(f"✓ 已解决问题 #{issue_index}")
    else:
        print(f"❌ 问题索引无效")


def main():
    """主函数"""
    import sys
    
    state = load_state()
    if not state:
        print("请先初始化项目：python init_context.py <项目名称>")
        sys.exit(1)
    
    if len(sys.argv) < 2:
        print("用法：python update_context.py <操作> [参数]")
        print("操作:")
        print("  phase <新阶段>     - 更新阶段")
        print("  add-issue <描述>   - 添加阻塞问题")
        print("  resolve-issue <ID> - 解决问题")
        print("  show              - 显示当前状态")
        sys.exit(1)
    
    action = sys.argv[1]
    
    if action == "phase" and len(sys.argv) > 2:
        update_phase(state, sys.argv[2])
        save_state(state)
    
    elif action == "add-issue" and len(sys.argv) > 2:
        severity = sys.argv[3] if len(sys.argv) > 3 else "medium"
        add_blocking_issue(state, sys.argv[2], severity)
        save_state(state)
    
    elif action == "resolve-issue" and len(sys.argv) > 2:
        resolve_blocking_issue(state, int(sys.argv[2]))
        save_state(state)
    
    elif action == "show":
        print("\n" + "="*60)
        print(f"📋 项目：{state['project_name']}")
        print(f"🔄 当前阶段：{state['current_phase']}")
        print(f"📊 进度：{state['completion_percentage']}%")
        print(f"📅 开始：{state['start_date']}")
        print(f"📌 下一步：{state.get('next_action', '暂无')}")
        
        if state["blocking_issues"]:
            print(f"\n⚠️ 阻塞问题 ({len(state['blocking_issues'])}):")
            for i, issue in enumerate(state["blocking_issues"]):
                if issue["status"] == "open":
                    print(f"   {i}. [{issue['severity']}] {issue['description']}")
        print("="*60)
    
    else:
        print(f"❌ 未知操作：{action}")


if __name__ == "__main__":
    main()
