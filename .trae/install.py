#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Trae 平台安装脚本
从 GitHub 下载 .trae 目录并安装到目标项目
"""

import os
import sys
import shutil
import tempfile
import zipfile
from pathlib import Path
from urllib.request import urlretrieve, urlopen


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


def download_trae_from_github(target_dir: Path):
    """从 GitHub 下载 .trae 目录"""
    # GitHub 仓库信息
    repo_owner = "WQuan0717"
    repo_name = "BaseSystem"
    branch = "trae-platform-test"
    
    print(f"🌐 从 GitHub 下载 .trae 目录...")
    print(f"   仓库：{repo_owner}/{repo_name}")
    print(f"   分支：{branch}")
    
    # 构建下载 URL
    zip_url = f"https://github.com/{repo_owner}/{repo_name}/archive/refs/heads/{branch}.zip"
    
    try:
        # 创建临时文件
        with tempfile.NamedTemporaryFile(suffix='.zip', delete=False) as tmp_file:
            temp_zip = tmp_file.name
        
        # 下载 ZIP 文件
        print(f"📥 正在下载...")
        urlretrieve(zip_url, temp_zip)
        
        # 解压 ZIP 文件
        print(f"📦 正在解压...")
        with zipfile.ZipFile(temp_zip, 'r') as zip_ref:
            # 获取 .trae 目录在 ZIP 中的路径
            trae_files = [f for f in zip_ref.namelist() if f.startswith(f'{repo_name}-{branch}/.trae/')]
            
            if not trae_files:
                print("❌ 在仓库中找不到 .trae 目录")
                sys.exit(1)
            
            # 解压 .trae 到临时目录
            temp_extract_dir = tempfile.mkdtemp()
            for file in trae_files:
                zip_ref.extract(file, temp_extract_dir)
        
        # 获取解压后的 .trae 路径
        extracted_trae = Path(temp_extract_dir) / f'{repo_name}-{branch}' / '.trae'
        
        # 目标位置
        trae_target = target_dir / ".trae"
        
        # 如果已存在，先备份
        if trae_target.exists():
            backup_path = target_dir / ".trae.backup"
            print(f"⚠️  备份现有的 .trae 到：{backup_path}")
            if backup_path.exists():
                shutil.rmtree(backup_path)
            shutil.move(str(trae_target), str(backup_path))
        
        # 复制 .trae 到目标目录
        print(f"📦 安装 .trae 到：{trae_target}")
        shutil.copytree(str(extracted_trae), str(trae_target))
        
        # 清理临时文件
        shutil.rmtree(temp_extract_dir)
        os.unlink(temp_zip)
        
        # 统计文件
        file_count = sum(1 for _ in trae_target.rglob("*") if _.is_file())
        print(f"✓ 已安装 {file_count} 个文件")
        
    except Exception as e:
        print(f"❌ 下载失败：{e}")
        print(f"\n💡 建议:")
        print(f"   1. 检查网络连接")
        print(f"   2. 手动从 GitHub 下载：{zip_url}")
        print(f"   3. 使用 git clone 方式获取完整项目")
        sys.exit(1)


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
    
    # 从 GitHub 下载 .trae 目录
    download_trae_from_github(target_dir)
    print()
    
    # 验证安装
    if not verify_installation(target_dir):
        print("\n❌ 安装失败，请检查错误信息")
        sys.exit(1)
    
    # 打印使用说明
    print_usage()


if __name__ == "__main__":
    main()
