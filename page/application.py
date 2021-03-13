# -*- coding: utf-8 -*-
"""
@Auth ： 王浩
@File ：application.py
@Email：whang27@163.com
"""
import allure
from appium import webdriver
from page.basepage import BasePage
from page.page_object.news_page import newsPage


class App(BasePage):
    def start(self):
        _package = "com.tencent.wework"
        _activity = ".launch.WwMainActivity"
        if self.driver is None:
            caps = {}
            caps["platformName"] = "Android"
            caps["platformVersion"] = "6.0"
            caps["deviceName"] = "MIX_2"
            caps["appPackage"] = _package
            caps["appActivity"] = _activity
            caps["noReset"] = True  # 保留上一次操作信息
            caps["autoGrantPermissions"] = True  # Appium自动授权app权限
            caps["unicodeKeyboard"] = True  # 解决无法输入中文问题
            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        else:
            # 复用之前的app服务，不用每次重启
            self.driver.start_activity(_package, _activity)
        self.driver.implicitly_wait(10)
        return self


    @allure.step("进入消息页面")
    def goto_newsPage(self):
        return newsPage(self.driver)