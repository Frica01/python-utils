# -*- coding: utf-8 -*-
# Name:         date_utils.py
# Author:       小菜
# Date:         2023/4/28 11:26
# Description:

from datetime import datetime, timedelta


def get_date_range(start_date, end_date, date_format='%Y-%m-%d', is_string=False) -> list:
    """
    取日期范围

    Args:
        start_date (str): 开始日期，格式为 YYYY-MM-DD
        end_date (str): 结束日期，格式为 YYYY-MM-DD
        date_format (str): 日期格式，默认为 '%Y-%m-%d'
        is_string (bool): 是否返回字符串类型的日期列表，默认为 True

    Raises:
        ValueError: 如果输入的日期格式错误，则会引发此异常

    Returns:
        list: 日期范围列表，如果 is_string 为 True，则返回字符串类型的日期列表，否则返回 datetime 类型的日期列表

    """

    try:
        start_date = datetime.strptime(start_date, date_format)
        end_date = datetime.strptime(end_date, date_format)
    except ValueError as e:
        raise ValueError(f"Invalid date format: {e}")

    date_list = list()
    while start_date <= end_date:
        if is_string:
            date_list.append(start_date.strftime(date_format))
        else:
            date_list.append(start_date)
        start_date += timedelta(days=1)
    return date_list


def date_diff_days(start_date, end_date) -> int:
    """
    计算两个日期之间的差异

    Args:
        start_date(str|datetime):
        end_date(str|datetime):

    Returns:
        int: 日期差异的天数

    """
    try:
        if isinstance(start_date, str):
            start_date = start_date.replace('/', '-')
            start_date = datetime.strptime(start_date, '%Y-%m-%d')
        if isinstance(end_date, str):
            end_date = end_date.replace('/', '-')
            end_date = datetime.strptime(end_date, '%Y-%m-%d')

        return (end_date - start_date).days
    except ValueError:
        raise ValueError(f"Invalid date format, input the YYYY-MM-DD")


def date_str_to_date(date_str: str, format_str='%Y-%m-%d') -> datetime:
    """
    将日期字符串转换为日期对象

    Args:
        date_str(str): 日期字符串，例如 '2000-01-01'
        format_str(str): 日期字符串的格式，默认为 '%Y-%m-%d'

    Returns:
        datetime: 转换后的日期对象
    """
    try:
        return datetime.strptime(date_str, format_str)
    except ValueError:
        raise ValueError(f"Invalid date format, input the YYYY-MM-DD")


