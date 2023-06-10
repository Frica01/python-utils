# -*- coding: utf-8 -*-
# Name:         html_utils.py
# Author:       小菜
# Date:         2023/4/28 11:25
# Description:

from typing import List

from installer import install_modules

install_modules(module_list=['lxml'])

from lxml import etree


def html_to_dom(html: str):
    return etree.HTML(html)


def extract_title(html_content: str) -> str:
    """从 HTML 内容中提取标题"""
    dom = html_to_dom(html_content)
    title = dom.xpath('//title/text()')[0]
    return title


def extract_links(html_content: str) -> List[str]:
    """从 HTML 内容中提取所有链接"""
    dom = html_to_dom(html_content)
    links = dom.xpath('//a/@href')
    return links


def parse_xpath(html_content: str, xpath_express: str = '.') -> List[etree.Element]:
    """从DOM中提取符合xpath表达式的节点列表"""
    dom = html_to_dom(html_content)
    if not xpath_express:
        raise ValueError("'xpath_express' parameter cannot be an empty string")
    return dom.xpath(xpath_express)

