#!/usr/bin/env python
# -*- coding: utf-8 -*-

__version__ = "0.0.1"
__author__ = "Zhongwei Sun (zhongwei.sun2008@gmail.com)"

# ----------------------------------------
# Just say "Hello world!".
# ----------------------------------------

# build-in, 3rd party and my modules
import re


def test_mongodb_id():
    url = "http://sunzhongwei.com/article/51bebc21d3115f25710afecf"
    pattern = r"\w{24}"
    article_id = re.search(pattern, url)
    print article_id.group()    # 51bebc21d3115f25710afecf


def test_date():
    s = "today is 2013-12-11"
    pattern = r"(\d{4}-\d{2}-\d{2})"
    date = re.search(pattern, s)
    print date.group()


if '__main__' == __name__:
    test_mongodb_id()
    test_date()

