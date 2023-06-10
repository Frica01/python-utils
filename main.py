# -*- coding: utf-8 -*-
# Name:         main.py
# Author:       小菜
# Date:         2023/4/28 13:49
# Description:

from utils import (date_utils, dict_to_excel)

if __name__ == '__main__':
    # 获取日期区间
    date_list = date_utils.get_date_range('2020-01-01', '2022-01-01')
    print(date_list)
    # 保存excel文件
    dict_to_excel(
        data_dict={'name': ['张三', '李四', '王五'], 'age': [18, 19, 20]},
        file_path='./demo.xlsx'
    )
