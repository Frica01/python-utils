# -*- coding: utf-8 -*-
# Name:         __init__.py
# Author:       小菜
# Date:         2023/4/28 11:23
# Description:

import os
import sys

from utils.config_utils import read_ini_config
from utils.date_utils import (
    get_date_range,
    date_diff_days,
    date_str_to_date
)
from utils.excel_utils import dict_to_excel
from utils.html_utils import (
    html_to_dom,
    extract_title,
    extract_links,
    parse_xpath
)
from utils.json_utils import (
    read_json,
    write_json,
    add_to_json,
    update_json,
    delete_from_json
)
from utils.network_utils import (
    build_url,
    send_request
)
from utils.os_utils import (
    check_file_exists,
    normalize_file_path,
    join_file_path
)
from utils.string_utils import replace_string
from utils.window_utils import (
    minimize_window,
    maximize_window,
    set_top_window,
    close_window,
    hide_window,
    show_window
)
