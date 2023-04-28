# -*- coding: utf-8 -*-
# Name:         string_utils.py
# Author:       小菜
# Date:         2023/4/28 11:25
# Description:

def replace_string(original_str, replace_map) -> str:
    """
    替换字符串中指定的内容

    Args:
        original_str(str): 原始字符串
        replace_map(dict): 替换字典，key为原字符串，value为替换字符串

    Returns:
        str:  替换后的字符串

    Examples:
        >>> replace_string("demo", {'d': 'b'})
        'bemo'
    """
    for old_str, new_str in replace_map.items():
        original_str = original_str.replace(old_str, new_str)

    return original_str
