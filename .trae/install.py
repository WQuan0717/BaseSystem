#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Trae 平台安装脚本
将 .trae 目录安装到目标项目
"""

import os
import sys
import shutil
from pathlib import Path


def check_python_version():
    """检查 Python 版本"""
    if sys.version_info < (3, 8):
        print("❌ 需要 Python 3.8 或更高版本")
        sys.exit(1)
    print(f"✓ Python 版本：{sys.version_info.major}.{sys.version_info.minor}")


def find_project_root():
    """查找项目根目录"""
    # 从当前目录开始
    current = Path.cwd()
    
    # 检查是否已经在项目中
    if (current / ".trae").exists():
        print(f"⚠️  当前目录已存在 .trae 文件夹")
        print(f"   位置：{current / '.trae'}")
        
        response = input("是否覆盖？(y/N): ")
        if response.lower() != 'y':
            print("❌ 安装取消")
            sys.exit(0)
    
    return current


def copy_trae_directory(target_dir: Path):
    """复制 .trae 目录"""
    # 获取脚本所在目录
    script_dir = Path(__file__).parent
    
    # 查找 .trae 目录
    trae_source = script_dir / ".trae"
    
    if not trae_source.exists():
        # 尝试从上级目录查找
        trae_source = script_dir.parent / ".trae"
    
    if not trae_source.exists():
        print("❌ 找不到 .trae 目录")
        print(f"   已尝试路径:")
        print(f"   - {trae_source}")
        sys.exit(1)
    
    print(f"✓ 找到 .trae 目录：{trae_source}")
    
    # 目标位置
    trae_target = target_dir / ".trae"
    
    # 如果已存在，先备份
    if trae_target.exists():
        backup_path = target_dir / ".trae.backup"
        print(f"⚠️  备份现有的 .trae 到：{backup_path}")
        if backup_path.exists():
            shutil.rmtree(backup_path)
        shutil.move(str(trae_target), str(backup_path))
    
    # 复制目录
    print(f"📦 复制 .trae 到：{trae_target}")
    shutil.copytree(str(trae_source), str(trae_target))
    
    # 统计文件
    file_count = sum(1 for _ in trae_target.rglob("*") if _.is_file())
    print(f"✓ 已复制 {file_count} 个文件")


def verify_installation(target_dir: Path):
    """验证安装"""
    print("\n🔍 验证安装...")
    
    trae_dir = target_dir / ".trae"
    
    # 检查必要目录
    required_dirs = [
        "rules",
        "skills"
    ]
    
    for dir_name in required_dirs:
        dir_path = trae_dir / dir_name
        if not dir_path.exists():
            print(f"❌ 缺少目录：{dir_name}")
            return False
        print(f"✓ {dir_name}/")
    
    # 检查核心 Skills
    core_skills = [
        "se-lifecycle",
        "se-context",
        "se-requirements",
        "se-architecture",
        "se-detailed-design",
        "se-development",
        "se-diagram",
        "se-testing",
        "se-documentation",
        "skill-creator"
    ]
    
    skills_dir = trae_dir / "skills"
    print("\n📦 检查核心 Skills:")
    
    for skill in core_skills:
        skill_path = skills_dir / skill
        if not skill_path.exists():
            print(f"❌ 缺少 Skill: {skill}")
            return False
        print(f"  ✓ {skill}/")
    
    # 检查规则文件
    rules_dir = trae_dir / "rules"
    print("\n📋 检查规则文件:")
    
    required_rules = [
        "user_rules.md",
        "project_rules.md"
    ]
    
    for rule_file in required_rules:
        rule_path = rules_dir / rule_file
        if not rule_path.exists():
            print(f"❌ 缺少规则：{rule_file}")
            return False
        print(f"  ✓ {rule_file}")
    
    print("\n✅ 安装验证通过!")
    return True


def print_usage():
    """打印使用说明"""
    print("\n" + "="*60)
    print("🎉 Trae 平台安装完成!")
    print("="*60)
    print("\n📚 下一步:")
    print("1. 查看安装文档：cat .trae/INSTALL.md")
    print("2. 初始化项目：python .trae/skills/se-context/scripts/init_context.py \"项目名称\"")
    print("3. 开始使用：在 Trae 中 invoke se-lifecycle")
    print("\n📦 核心 Skills:")
    print("  - se-lifecycle       工作流决策")
    print("  - se-context         状态管理")
    print("  - se-development     开发实现")
    print("  - se-testing         测试验证")
    print("\n💡 提示:")
    print("  在 Trae 对话中使用 'invoke se-xxx' 调用 Skills")
    print("="*60)


def main():
    """主函数"""
    print("="*60)
    print("🚀 Trae 平台安装程序")
    print("="*60)
    print()
    
    # 检查 Python 版本
    check_python_version()
    print()
    
    # 查找项目根目录
    target_dir = find_project_root()
    print(f"📁 目标目录：{target_dir}")
    print()
    
    # 复制 .trae 目录
    copy_trae_directory(target_dir)
    print()
    
    # 验证安装
    if not verify_installation(target_dir):
        print("\n❌ 安装失败，请检查错误信息")
        sys.exit(1)
    
    # 打印使用说明
    print_usage()


if __name__ == "__main__":
    main()
