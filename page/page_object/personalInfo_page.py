# -*- coding: utf-8 -*-
"""
@Auth ： 王浩
@File ：personalInfo_page.py
@Email：whang27@163.com
"""
import allure
from page.basepage import BasePage
from page.page_object.infoSettings_page import InfoSettingsPage

class PersonalInfoPage(BasePage):

    @allure.step("进入成员设置页面")
    def goto_InfoSettings(self):
        self.parse_action('personalInfo_page.yaml', 'goto_InfoSettings')
        return InfoSettingsPage(self.driver)
