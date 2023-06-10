# -*- coding: utf-8 -*-
# Name:         os_utils.py
# Author:       小菜
# Date:         2023/5/16 16:57
# Description:


import os
from typing import Union


def check_file_exists(path: str) -> bool:
    """
    检查文件是否存在

    Args:
        path (str): 文件路径

    Returns:
        bool: 文件是否存在，存在返回 True，否则返回 False
    """
    return os.path.exists(path=path)


def normalize_file_path(path: str) -> Union[str, bool]:
    """
    标准化文件路径

    Args:
        path (str): 文件路径

    Returns:
        Union[str, bool]: 标准化后的文件路径，如果文件不存在则返回 False
    """
    if not check_file_exists(path):
        return False
    return os.path.normpath(path=path)


def join_file_path(base_path: str, file_name: str) -> Union[str, bool]:
    """
    拼接文件路径

    Args:
        base_path (str): 基础路径
        file_name (str): 文件名

    Returns:
        Union[str, bool]: 拼接后的文件路径，如果基础路径不存在则返回 False
    """
    if not check_file_exists(base_path):
        return False
    return normalize_file_path(os.path.join(base_path, file_name))

# TODO
# 读取和写入文件、复制和移动文件、创建和删除目录
