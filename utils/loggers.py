# -*- coding: utf-8 -*-
"""
@Auth ： 王浩
@File ：loggers.py
@Email：whang27@163.com
"""
import logging
import os
import time
from utils import setting


# 日志存放路径
log_path = setting.TEST_LOG
# 若不存在日志文件就新建一个
if not os.path.exists(log_path): os.mkdir(log_path)

class Logger:

    def __init__(self):
        # 文件的命名
        self.logName = os.path.join(log_path, "%s.log" % time.strftime("%Y%m%d%H"))
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        # 日志输出格式
        self.formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s : %(message)s')

    def __console(self, level, message):
        # 创建一个FileHandler，用于写到本地,追加
        fh = logging.FileHandler(self.logName, "a", encoding='utf-8')
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(self.formatter)
        self.logger.addHandler(fh)

        # 创建一个StreamHandler,用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch)

        if level == "info":
            self.logger.info(message)
        elif level == "debug":
            self.logger.debug(message)
        elif level == "warning":
            self.logger.warning(message)
        elif level == "error":
            self.logger.error(message)

        # 这两行代码是为了避免日志输出重复问题
        self.logger.removeHandler(ch)
        self.logger.removeHandler(fh)

        # 关闭打开的文件
        fh.close()

    def debug(self, message):
        self.__console("debug", message)

    def info(self, message):
        self.__console("info", message)

    def warning(self, message):
        self.__console("warning", message)

    def error(self, message):
        self.__console("error", message)


if __name__ == "__main__":
    log = Logger()
    log.info("--测试开始--")
    log.info("操作步骤1，2,3")
    log.warning("--测试结束--")