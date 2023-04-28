# -*- coding: utf-8 -*-
# Name:         main.py
# Author:       小菜
# Date:         2023/4/28 13:49
# Description:

from utils import date_utils

if __name__ == '__main__':
    date_list = date_utils.get_date_range('2020-01-01', '2022-01-01')
    print(date_list)
