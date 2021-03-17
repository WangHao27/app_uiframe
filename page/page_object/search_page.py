# -*- coding: utf-8 -*-
"""
@Auth ： 王浩
@File ：search_page.py
@Email：whang27@163.com
"""
import allure

from page.basepage import BasePage
from page.page_object.personalInfo_page import PersonalInfoPage


class SearchPage(BasePage):

    @allure.step("获取页面所有成员数量")
    def get_membersNumber(self, memberName):
        self._params['memberName'] = memberName
        members_list = self.parse_action('search_page.yaml', 'get_membersNumber')
        return members_list

    @allure.step("进入个人信息页面")
    def goto_personalInfo(self):
        self.parse_action('search_page.yaml', 'goto_personalInfo')
        return PersonalInfoPage(self.driver)