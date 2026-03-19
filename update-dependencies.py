#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @License  ：(C)Copyright 2025, 数道智融科技
# @Author   ：李锋
# @Software ：PyCharm
# @Date     ：2026/3/19 下午3:55
# @Desc     ：简单的依赖管理工具 - 从pyproject.toml读取依赖，生成 uv remove和uv add 操作命令

import sys
from pathlib import Path
from typing import Set

try:
    import tomli
except ImportError:
    print("\n❌ 错误: 请先安装tomli库", file=sys.stderr)
    print("    pip install tomli\n", file=sys.stderr)
    sys.exit(1)


def read_dependencies(pyproject_path: str = "pyproject.toml") -> Set[str]:
    """
    从pyproject.toml读取依赖列表
    """
    pyproject_file = Path(pyproject_path)

    if not pyproject_file.exists():
        print(f"\n❌ 错误: 找不到文件 '{pyproject_path}'\n")
        sys.exit(1)

    with open(pyproject_file, "rb") as f:
        data = tomli.load(f)

    dependencies = set()

    # 标准项目依赖
    if "project" in data and "dependencies" in data["project"]:
        for dep in data["project"]["dependencies"]:
            # 提取包名（去除版本号）
            pkg_name = dep.split(">=")[0].split("==")[0].split("~=")[0].split("!=")[0].split("[")[0].strip()
            if pkg_name:
                dependencies.add(pkg_name)

    # Poetry项目依赖
    if "tool" in data and "poetry" in data["tool"]:
        poetry_deps = data["tool"]["poetry"].get("dependencies", {})
        for pkg_name in poetry_deps.keys():
            if pkg_name != "python":
                dependencies.add(pkg_name)

    return dependencies


def main():
    """主函数"""
    import argparse
    parser = argparse.ArgumentParser(description="简单的依赖管理工具")
    parser.add_argument("-f", "--file", default="pyproject.toml", help="pyproject.toml文件路径")
    parser.add_argument("-y", "--yes", action="store_true", help="自动确认")
    args = parser.parse_args()

    # 读取依赖
    deps = read_dependencies(args.file)

    if not deps:
        print("⚠️  没有找到任何依赖")
        return

    deps_list = sorted(deps)

    # 显示找到的依赖
    print(f"\n📋 找到 {len(deps_list)} 个依赖:")
    for i, dep in enumerate(deps_list, 1):
        print(f"   {i:2d}. {dep}")

    # 确认操作
    if not args.yes:
        print(f"\n复制下面命令到终端执行:")
        print(f"uv remove {' '.join(deps_list)}")
        print(f"uv add {' '.join(deps_list)}")


if __name__ == "__main__":
    main()
