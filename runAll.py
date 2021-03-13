# -*- coding: utf-8 -*-
"""
@Auth ： 王浩
@File ：runAll.py
@Email：whang27@163.com
"""
import os
import time
from utils.setting import TEST_REPORT, TESTCASES_DIR

if __name__ == "__main__":
    print('开始生成测试报告'.center(45, '*'))
    os.system('pytest ' + '--alluredir=' + TEST_REPORT)
    time.sleep(3)
    os.system('allure generate ' + TEST_REPORT + ' -o ' + TESTCASES_DIR + ' --clean')
    print('测试报告生成完毕'.center(45, '*'))

