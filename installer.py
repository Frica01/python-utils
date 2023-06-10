# -*- coding: utf-8 -*-
# @Author : Frica01
# @Time   : 2023-06-10 16:54
# @Name   : installer.py


import importlib
import subprocess


def install_module(module_name: str):
    """
    安装指定的模块，如果模块不存在则进行安装.

    Args:
        module_name(str): 要安装的模块名称。

    Returns:
        bool: 指示安装是否成功的布尔值。
    """
    try:
        # 尝试导入模块
        importlib.import_module(module_name)
    except ImportError:
        # 构建 pip 命令参数
        args = ['pip', 'install', '-i', 'https://pypi.doubanio.com/simple/', module_name]
        try:
            # 调用 pip 命令进行安装
            subprocess.check_call(args)
            print(f'{module_name} 模块安装成功.')
            return True
        except subprocess.CalledProcessError:
            print(f'{module_name} 模块安装失败.')
            return False


def install_modules(module_list: list):
    """
    安装指定的模块列表。

    Args:
        module_list(list): 要安装的模块列表。

    Returns:

    """
    for module_name in module_list:
        install_module(module_name=module_name)
