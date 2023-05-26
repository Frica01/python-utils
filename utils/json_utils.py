# -*- coding: utf-8 -*-
# Name:         json_utils.py
# Author:       小菜
# Date:         2023/4/28 11:23
# Description:

import os
import json
from typing import Union


def read_json(file_path: str) -> Union[list, dict]:
    """读取json"""

    # 先判断json文件是否存在
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"{file_path} not found.")
    with open(file_path, 'r', encoding='utf-8') as f:
        json_data: Union[list, dict] = json.load(f)
    return json_data


def write_json(data, file_path: str) -> None:
    """

    Args:
        data(Union[dict, list]): 需要写入文件的数据
        file_path(str): 文件路径

    Raises:
        ValueError: 数据不符合 JSON 格式，或文件路径不合法。
        IOError: 写入文件失败。

    """
    #  检查文件名称是否合法
    if not file_path.endswith('.json'):
        raise IOError(f"file_path error!")

    # 检查数据是否可以转换为 JSON 格式
    try:
        json.dumps(data)
    except (TypeError, ValueError) as e:
        raise ValueError(f"Invalid JSON data: {e}")

    # 检查文件路径是否合法
    file_dir = os.path.dirname(file_path)
    file_name = os.path.basename(file_path)
    if not os.path.exists(file_dir):  # 判断路径是否存在
        raise FileNotFoundError(f"Directory {file_dir} not found")
    if not os.path.isdir(file_dir):  # 判断路径是否为目录
        raise NotADirectoryError(f"{file_dir} is not a directory")
    if any(c in file_name for c in r'<>:"/\|?*'):  # 名字中不能包含特殊字符串
        raise ValueError(f"Invalid characters in file path: {file_path}")

    # 写入文件
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
    except OSError as e:
        raise IOError(f"Failed to write JSON file: {e}")


def add_to_json(file_path: str, data: dict) -> None:
    """
    向JSON文件中添加数据

    Args:
        file_path (str): JSON文件路径
        data (dict): 要添加的数据

    Raises:
        FileNotFoundError: 如果指定的文件不存在，则抛出此异常
        JSONDecodeError: 如果JSON文件解码失败，则抛出此异常
    """

    # 先读取原有的数据
    original_data = read_json(file_path)

    # 将新数据添加到原有数据中
    original_data.append(data)

    # 将合并后的数据写入文件中
    write_json(original_data, file_path=file_path)


def update_json(file_path, update_map, key) -> None:
    """修改JSON文件中的数据

    Args:
        file_path(str): JSON文件路径
        update_map(dict): 需要更新的数据，是一个字典类型
        key(str): 指定用于查找需要更新的数据的键名

    Raises:
        KeyError: 如果找不到指定的键名，则抛出 KeyError 异常

    """
    try:
        # 先读取原有的数据
        original_data = read_json(file_path)

        # 根据指定的 key 找到需要修改的数据
        for item in original_data:
            if item[key] == update_map[key]:
                # 更新数据
                item.update(update_map)
        # 将修改后的数据写入文件中

        write_json(original_data, file_path=file_path)
    except KeyError:
        raise ValueError(f"File read/write error")


def delete_from_json(file_path, key) -> None:
    """
    从JSON文件中删除指定 key 的数据

    Args:
        file_path (str): JSON文件路径
        key (str): 需要删除的数据的 key
    """
    # 先读取原有的数据
    original_data = read_json(file_path)

    # 找到需要删除的数据
    for _key in original_data:
        if key == _key:
            # 删除数据
            del original_data[_key]

    # 将剩余的数据写入文件中
    write_json(file_path, original_data)
