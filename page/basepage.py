# -*- coding: utf-8 -*-
"""
@Auth ： 王浩
@File ：basepage.py
@Email：whang27@163.com
"""
import json
import os
import allure
import yaml
from time import sleep
from typing import Dict, List
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
from utils import setting
from utils.loggers import Logger

log = Logger()
shot_path = setting.SCREEN_SHOT
class BasePage:
    _params = {}
    _error_count = 0
    _error_max = 10
    _black_list = [(By.XPATH, "//*[@text='关闭']"), (By.XPATH, "//*[@resource-id='com.tencent.wework:id/bpc']")]

    def __init__(self, driver: WebDriver=None):
        self.driver = driver

    def find(self, by, locator=None):
        try:
            element = self.driver.find_element(*by) if isinstance(by, tuple) else self.driver.find_element(by, locator)
            # 找到元素后重置错误次数
            self._error_count = 0
            self.driver.implicitly_wait(10)
            return element
        except Exception as e:
            log.warning(f"元素：by={by} locator={locator} 未找到，开始黑名单处理...")
            self._error_count += 1
            # 减少黑名单处理等待时间
            self.driver.implicitly_wait(2)
            # 保存出现错误页面的截图
            self.driver.get_screenshot_as_file(f"{shot_path}/tmp.png")
            allure.attach.file("tmp.png", attachment_type=allure.attachment_type.PNG)
            # 设置最大查找次数
            if self._error_count > self._error_max:
                log.error(f"需要的元素：by={by} locator={locator}，未找到，请处理...")
                raise e
            for black in self._black_list:
                # 查找当前弹窗是否存在于黑名单中，存在则点击关闭，返回函数本身
                elements = self.driver.find_elements(*black)
                if len(elements) > 0:
                    elements[0].click()
                    log.info(f"黑名单元素：{elements[0]}已处理!")
                    return self.find(by, locator)
            raise e

    # 滑动查找并点击
    def swip_click(self, text):
        self.find(MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable(true).instance(0)).'
                                                'scrollIntoView(new UiSelector().'
                                                f'text("{text}").instance(0));').click()
        log.info(f"元素：{text}，已找到...")

    def send(self, value, by, locator):
        self.find(by, locator).click()
        self.find(by, locator).send_keys(value)
        log.info(f"元素：by={by} locator={locator}，输入值为：{value}")

    def parse_action(self, path, func_name):
        global element, value
        # 加入yaml文件读取路径
        path = os.path.join(setting.PAGE_YAML, path)
        with open(path, 'r', encoding="utf-8") as f:
            function = yaml.safe_load(f)
            steps: List[Dict] = function[func_name]

        # 将需要替换的值提前替换
        # json.dumps() 序列化  python 对象转化成字符串
        # json.loads() 反序列化  python 字符串转化为python对象
        raw = json.dumps(steps)
        for key, value in self._params.items():
            raw = raw.replace("${%s}" % key, value)
        steps = json.loads(raw)
        for step in steps:
            if "by" in step.keys():
                element = self.find(step['by'], step['locator'])
            if "action" in step.keys():
                if "click" == step["action"]:
                    log.info(f"点击元素：{element.text}")
                    element.click()
                if "swip_click" == step["action"]:
                    self.swip_click(step["text"])
                if "send" == step["action"]:
                    self.send(step["value"], step['by'], step['locator'])
                if "sleep" == step["action"]:
                    time = int(step["time"])
                    sleep(time)