# -*- coding: utf-8 -*-
# Name:         network_utils.py
# Author:       小菜
# Date:         2023/4/28 11:23
# Description:

from installer import install_modules

install_modules(module_list=['requests'])

import json
import requests

from typing import Union
from urllib import parse


def build_url(url, params) -> str:
    """
    构建带参数的URL

    Args:
        url (str): URL地址
        params (dict): 参数字典

    Returns:
        str: 带参数的URL
    """
    if not params:
        return url
    query_string = parse.urlencode(params)
    return f'{url}?{query_string}'


def send_request(url, method='get', *args, **kwargs) -> Union[str, dict]:
    """
    发送网络请求, 默认方法为GET(只对GET 和 POST请求做匹配)根据结果返回str或json

    Args:
        url (str): 请求的url地址
        method (str): 请求方法，默认为 'get', 可选 get、post
        *args: 传递给requests库的其他参数
        **kwargs: 传递给requests库的其他关键字参数

    Returns:
        Union[str, dict]: 根据请求结果返回字符串或者字典

    Raises:
        Timeout,ConnectTimeout: 请求超时或连接错误
    """

    try:
        if method in ['get', 'Get', 'GET']:
            response = requests.get(url, *args, **kwargs)
        elif method in ['post', 'Post', 'POST']:
            response = requests.post(url, *args, **kwargs)
        else:
            raise ValueError(f"HTTP方法 {method} 不受支持。")

        # 如果响应状态码不是200，则会引发HTTPError异常
        response.raise_for_status()

    except requests.exceptions.ConnectTimeout:
        raise requests.exceptions.ConnectTimeout(f"ConnectTimeout.")

    except requests.exceptions.ReadTimeout:
        raise requests.exceptions.ReadTimeout(f"ReadTimeout.")

    except requests.exceptions.Timeout:
        raise requests.exceptions.Timeout(f"Timeout.")

    except requests.exceptions.ConnectionError:
        raise requests.exceptions.ConnectionError(f"ConnectionError.")

    try:
        result = response.json()
    except (ValueError, json.JSONDecodeError):
        result = response.text

    return result


def upload_file(url, file_path) -> dict:
    """
    将本地文件上传到指定URL，并使用POST请求在请求体中包含文件数据。

    Args:
    - url (str): 上传文件的目标URL。
    - file_path (str): 要上传的本地文件路径。

    Returns:
    一个字典，包含从服务器解析的JSON响应。

    Raises:
    - requests.exceptions.RequestException: 发送请求或接收响应时出现错误。
    - FileNotFoundError: 如果指定的file_path路径下没有找到文件，则引发此异常。
    """
    try:
        with open(file_path, 'rb') as file:
            response = requests.post(url, files={'file': file})
            # 如果响应状态码不是200，则会引发HTTPError异常
            response.raise_for_status()
        return response.json()
    except FileNotFoundError:
        raise FileNotFoundError(f"file {file_path} not found")
    except requests.exceptions.RequestException:
        raise requests.exceptions.RequestException("RequestException.")


def download_file(url, file_path):
    """
    从指定URL下载文件，并将其保存到本地

    Args:
        url(str): 要下载的文件的URL
        file_path (str): 要保存下载文件的本地路径

    Returns:
        下载文件的本地路径

    Raises:
        requests.exceptions.RequestException: 发送请求或接收响应时出现错误
        IOError: 写入文件时出现错误
    """

    try:
        response = requests.get(url, stream=True)
        # 如果响应状态码不是200，则会引发HTTPError异常
        response.raise_for_status()
        with open(file_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    file.write(chunk)
        return file_path
    except requests.exceptions.RequestException:
        raise requests.exceptions.RequestException("RequestException.")
    except IOError:
        raise IOError(f"IOError. write {file_path} error")
