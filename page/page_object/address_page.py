# -*- coding: utf-8 -*-
"""
@Auth ： 王浩
@File ：address_page.py
@Email：whang27@163.com
"""
import allure
from page.basepage import BasePage
from page.page_object.addmembers_page import AddMembersPage
from page.page_object.personalInfo_page import PersonalInfoPage


class AddressListPage(BasePage):

    @allure.step("进入个人信息页面")
    def goto_personalInfo(self, name):
        self._params['name'] = name
        self.parse_action('address_page.yaml', 'goto_personalInfo')
        return PersonalInfoPage(self.driver)

    @allure.step("进入添加成员界面")
    def goto_addmenbers(self):
        self.parse_action('address_page.yaml', 'goto_addmenbers')
        return AddMembersPage(self.driver)
