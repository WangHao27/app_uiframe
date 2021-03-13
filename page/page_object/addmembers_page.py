# -*- coding: utf-8 -*-
"""
@Time ： 2021/3/7 15:16
@Auth ： wanghao
@File ：addmembers_page.py
"""
import allure
from page.basepage import BasePage
from page.page_object.savemember_page import SaveMembersPage


class AddMembersPage(BasePage):

    @allure.step("进入保存成员界面")
    def goto_savemembers(self):
        self.parse_action("addmembers_page.yaml", "goto_savemembers")
        return SaveMembersPage(self.driver)
