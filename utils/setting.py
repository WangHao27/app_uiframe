# -*- coding: utf-8 -*-
"""
@Auth ： 王浩
@File ：setting.py
@Email：whang27@163.com
"""
import os, sys


"""
文件路径配置
"""
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)

# 日志文件存放路径
TEST_LOG = os.path.join(BASE_DIR, "report/logs")
# page_yaml文件路径
PAGE_YAML = os.path.join(BASE_DIR, "page/page_yaml")
# testdata文件路径
TEST_DATA = os.path.join(BASE_DIR, "testdata")
# 测试报告数据
TEST_REPORT = os.path.join(BASE_DIR, "report")
# 测试报告路径
TESTCASES_DIR = os.path.join(BASE_DIR, "report/html")
# 测试截图路径
SCREEN_SHOT = os.path.join(BASE_DIR, "report/screenshot")
