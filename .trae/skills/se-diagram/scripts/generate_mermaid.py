#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
生成 Mermaid 图表
从文本描述或设计文档生成 Mermaid 语法
"""

import os
from pathlib import Path


def generate_usecase_diagram(actors: list, usecases: list, system_name: str = "系统"):
    """生成用例图"""
    
    mermaid = ["usecaseDiagram"]
    mermaid.append(f'    title {system_name} 用例图')
    mermaid.append("")
    
    # 添加参与者
    for i, actor in enumerate(actors, 1):
        mermaid.append(f'    actor "{actor["name"]}" as A{i}')
        if "description" in actor:
            mermaid.append(f'    note right of A{i}: {actor["description"]}')
    
    mermaid.append("")
    mermaid.append(f'    package "{system_name}" {{')
    
    # 添加用例
    for i, uc in enumerate(usecases, 1):
        mermaid.append(f'        usecase "{uc["name"]}" as UC{i}')
    
    mermaid.append("    }")
    mermaid.append("")
    
    # 添加关系
    for i, actor in enumerate(actors, 1):
        if "usecases" in actor:
            for uc_idx in actor["usecases"]:
                mermaid.append(f"    A{i} --> UC{uc_idx}")
    
    return "\n".join(mermaid)


def generate_er_diagram(entities: list, title: str = "ER 图"):
    """生成 ER 图"""
    
    mermaid = ["erDiagram"]
    mermaid.append(f'    title {title}')
    mermaid.append("")
    
    for entity in entities:
        entity_name = entity["name"]
        mermaid.append(f"    {entity_name} {{")
        
        for attr in entity.get("attributes", []):
            type_ = attr.get("type", "string")
            name = attr["name"]
            if attr.get("primary_key"):
                mermaid.append(f"        {type_} {name} PK")
            elif attr.get("foreign_key"):
                mermaid.append(f"        {type_} {name} FK")
            else:
                mermaid.append(f"        {type_} {name}")
        
        mermaid.append("    }")
        mermaid.append("")
    
    # 添加关系
    for entity in entities:
        if "relations" in entity:
            for rel in entity["relations"]:
                from_card = rel.get("from_card", "||")
                to_card = rel.get("to_card", "||")
                rel_name = rel.get("name", "has")
                mermaid.append(f'    {entity["name"]} {from_card}--{to_card} {rel["to"]} : "{rel_name}"')
    
    return "\n".join(mermaid)


def generate_class_diagram(classes: list, title: str = "类图"):
    """生成类图"""
    
    mermaid = ["classDiagram"]
    mermaid.append(f'    title {title}')
    mermaid.append("")
    
    for cls in classes:
        class_name = cls["name"]
        mermaid.append(f"    class {class_name} {{")
        
        # 属性
        for attr in cls.get("attributes", []):
            visibility = attr.get("visibility", "+")
            type_ = attr.get("type", "any")
            name = attr["name"]
            mermaid.append(f"        {visibility}{name}: {type_}")
        
        # 方法
        for method in cls.get("methods", []):
            visibility = method.get("visibility", "+")
            return_type = method.get("return", "void")
            name = method["name"]
            params = ", ".join(method.get("params", []))
            mermaid.append(f"        {visibility}{name}({params}) {return_type}")
        
        mermaid.append("    }")
        mermaid.append("")
    
    # 添加关系
    for cls in classes:
        if "relations" in cls:
            for rel in cls["relations"]:
                rel_type = rel.get("type", "--")
                mermaid.append(f'    {cls["name"]} {rel_type} {rel["to"]} : {rel.get("label", "")}')
    
    return "\n".join(mermaid)


def generate_flowchart(steps: list, title: str = "流程图"):
    """生成流程图"""
    
    mermaid = ["flowchart TD"]
    mermaid.append(f'    title {title}')
    mermaid.append("")
    
    for i, step in enumerate(steps):
        step_id = f"S{i+1}"
        label = step["label"]
        shape = step.get("shape", "rect")
        
        if shape == "rect":
            mermaid.append(f'    {step_id}[{label}]')
        elif shape == "round":
            mermaid.append(f'    {step_id}([{label}])')
        elif shape == "diamond":
            mermaid.append(f'    {step_id}{{{label}}}')
        elif shape == "doc":
            mermaid.append(f'    {step_id}[({label})]')
    
    mermaid.append("")
    
    # 添加流程
    for i in range(len(steps) - 1):
        from_id = f"S{i+1}"
        to_id = f"S{i+2}"
        label = steps[i].get("next_label", "")
        if label:
            mermaid.append(f"    {from_id} -->|{label}| {to_id}")
        else:
            mermaid.append(f"    {from_id} --> {to_id}")
    
    return "\n".join(mermaid)


def save_diagram(content: str, filename: str, output_dir: str = "docs/diagrams"):
    """保存图表文件"""
    
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    filepath = os.path.join(output_dir, filename)
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    
    print(f"✓ 图表已保存：{filepath}")
    return filepath


if __name__ == "__main__":
    # 示例：生成用例图
    actors = [
        {"name": "用户", "description": "系统使用者", "usecases": [1, 2]},
        {"name": "管理员", "description": "系统管理者", "usecases": [2, 3]}
    ]
    
    usecases = [
        {"name": "登录"},
        {"name": "管理数据"},
        {"name": "查看报表"}
    ]
    
    content = generate_usecase_diagram(actors, usecases, "管理系统")
    save_diagram(content, "usecase.mmd")
    print(content)
