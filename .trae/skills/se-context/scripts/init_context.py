#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
初始化项目状态
创建 docs/context/ 目录结构和初始状态文件
"""

import json
import os
from datetime import datetime
from pathlib import Path


def init_context(project_name: str, project_type: str = "web_app"):
    """初始化项目上下文"""
    
    # 创建目录结构
    dirs = [
        "docs/context",
        "docs/context/history"
    ]
    
    for dir_path in dirs:
        Path(dir_path).mkdir(parents=True, exist_ok=True)
        print(f"✓ 创建目录：{dir_path}")
    
    # 初始化项目状态
    state = {
        "project_name": project_name,
        "project_type": project_type,
        "current_phase": "init",
        "completed_phases": [],
        "pending_phases": ["requirements", "architecture", "design", "development", "testing", "documentation"],
        "completion_percentage": 0,
        "tech_stack": {
            "frontend": "",
            "backend": "",
            "database": "",
            "others": []
        },
        "start_date": datetime.now().strftime("%Y-%m-%d"),
        "target_date": "",
        "last_updated": datetime.now().isoformat(),
        "blocking_issues": [],
        "next_action": "开始需求分析"
    }
    
    # 保存项目状态
    state_path = "docs/context/project_state.json"
    with open(state_path, "w", encoding="utf-8") as f:
        json.dump(state, f, ensure_ascii=False, indent=2)
    print(f"✓ 创建文件：{state_path}")
    
    # 备份历史
    history_path = f"docs/context/history/state_{datetime.now().strftime('%Y-%m-%d_%H%M%S')}.json"
    with open(history_path, "w", encoding="utf-8") as f:
        json.dump(state, f, ensure_ascii=False, indent=2)
    print(f"✓ 创建历史备份：{history_path}")
    
    print("\n✅ 项目上下文初始化完成!")
    return state


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("用法：python init_context.py <项目名称> [项目类型]")
        sys.exit(1)
    
    project_name = sys.argv[1]
    project_type = sys.argv[2] if len(sys.argv) > 2 else "web_app"
    init_context(project_name, project_type)
