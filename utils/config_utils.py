# -*- coding: utf-8 -*-
# Name:         config_utils.py
# Author:       小菜
# Date:         2023/4/28 11:23
# Description:

import os
import configparser


def read_ini_config(file_path: str, section: str) -> dict:
    """
    读取 ini 配置文件中指定节的配置信息

    Args:
        file_path(str): 配置文件路径
        section(str): 节名称

    Returns:
        dict: 节配置信息

    Raises:
        FileNotFoundError: 配置文件不存在
        configparser.NoSectionError: 节不存在

    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Config file {file_path} not found.")

    config = configparser.ConfigParser()
    config.read(file_path, encoding='utf-8')

    if not config.has_section(section):
        raise configparser.NoSectionError(f"Section {section} not found in config file.")

    section_config = dict(config[section])
    return section_config
