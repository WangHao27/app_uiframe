# -*- coding: utf-8 -*-
"""
@Time ： 2021/3/7 15:17
@Auth ： wanghao
@File ：savemember_page.py
"""
import allure
from page.basepage import BasePage


class SaveMembersPage(BasePage):

    @allure.step("保存成员信息")
    def savemembers(self, name, phone):
        self._params['name'] = name
        self._params['phone'] = phone
        self.parse_action("savemember_page.yaml", "savemembers")