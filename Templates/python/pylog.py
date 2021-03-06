#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import os.path
import logging


# ----------------------------------------
# logging setting
# 避免与 web 接口的 logging 冲突
# 但是如果 web 接口使用的是logging, 而不是 logger，下面的日志会被记录两份
# ----------------------------------------
LOG_DIR = "/data/logs/test/"
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)
LOG_FILE_PATH = os.path.join(LOG_DIR,
        "test.log")
logger = logging.getLogger(__name__)
file_handler = logging.FileHandler(LOG_FILE_PATH)
formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


if __name__ == "__main__":
    logger.info("Hello world!")
