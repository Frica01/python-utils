# -*- coding: utf-8 -*-
# Name:         window_utils.py
# Author:       小菜
# Date:         2023/4/28 14:23
# Description:

import platform

# 判断当前系统平台是 Windows
if 'Windows' == platform.system():
    from installer import install_modules

    install_modules(module_list=['pywin32'])
else:
    raise SystemError('Windows系统才可调用噢！')

import win32gui
import win32con


# 窗口定位


def get_window_handle(class_name=None, title=None):
    """
    通过类名和标题查找窗口句柄.

    Args:
        class_name(str|None):窗口的类名. 默认为None.
        title(str|None):窗口的标题. 默认为None.

    Returns:
        int: 返回找到的窗口句柄，如果没有找到则返回0.
    """
    return win32gui.FindWindow(class_name, title)


# 窗口最小化
def minimize_window(class_name=None, title=None):
    """
    窗口最小化

    Args:
        class_name(str|None):窗口的类名. 默认为None.
        title(str|None):窗口的标题. 默认为None.

    Returns:
        None
    """
    hwnd = get_window_handle(class_name=class_name, title=title)
    win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE)


# 窗口最大化
def maximize_window(class_name=None, title=None):
    """
    窗口最大化

    Args:
        class_name(str|None):窗口的类名. 默认为None.
        title(str|None):窗口的标题. 默认为None.

    Returns:
        None
    """
    hwnd = get_window_handle(class_name=class_name, title=title)
    win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)


# 窗口置顶
def set_top_window(class_name=None, title=None):
    """
    窗口置顶

    Args:
        class_name(str|None):窗口的类名. 默认为None.
        title(str|None):窗口的标题. 默认为None.

    Returns:
        None
    """
    hwnd = get_window_handle(class_name=class_name, title=title)
    win32gui.SetForegroundWindow(hwnd)


# 关闭窗口
def close_window(class_name=None, title=None):
    """
    关闭窗口

    Args:
        class_name(str|None):窗口的类名. 默认为None.
        title(str|None):窗口的标题. 默认为None.

    Returns:
        None
    """
    hwnd = get_window_handle(class_name=class_name, title=title)
    win32gui.CloseWindow(hwnd)


# 隐藏窗口
def hide_window(class_name=None, title=None):
    """
    隐藏窗口

    Args:
        class_name(str|None):窗口的类名. 默认为None.
        title(str|None):窗口的标题. 默认为None.

    Returns:
        None
    """
    hwnd = get_window_handle(class_name=class_name, title=title)
    win32gui.ShowWindow(hwnd, win32con.SW_HIDE)


# 显示窗口
def show_window(class_name=None, title=None):
    """
    显示窗口

    Args:
        class_name(str|None):窗口的类名. 默认为None.
        title(str|None):窗口的标题. 默认为None.

    Returns:
        None
    """
    hwnd = get_window_handle(class_name=class_name, title=title)
    win32gui.ShowWindow(hwnd, win32con.SW_SHOW)


if __name__ == '__main__':
    show_window('WeChatMainWndForPC', '微信')
    maximize_window('WeChatMainWndForPC', '微信')

