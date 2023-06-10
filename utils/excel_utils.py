# -*- coding: utf-8 -*-
# Name:         excel_utils.py
# Author:       小菜
# Date:         2023/5/26 15:41
# Description:

"""
安装pandas、dict_to_excel
"""

from installer import install_modules

install_modules(module_list=['pandas', 'openpyxl'])

import pandas as pd


def dict_to_excel(data_dict: dict, file_path: str) -> None:
    """
    将字典数据添加到Excel文件中。

    Args：
        data_dict (dict): 包含要添加到Excel文件的数据的字典。
                          字典的键（key）为列名称，值（value）为对应的内容。
                          默认格式为dict(str:list()...)
        file_path (str): Excel文件的路径。

    Returns：
        None
    """

    # 将字典数据转换为DataFrame
    df = pd.DataFrame.from_dict(data_dict, orient='index').transpose()

    # 尝试读取现有的Excel文件，如果文件不存在则创建新文件
    try:
        existing_data = pd.read_excel(file_path)
        df = pd.concat([existing_data, df], ignore_index=True)
    except FileNotFoundError:
        pass

    # 将DataFrame写入Excel文件
    df.to_excel(file_path, index=False)
