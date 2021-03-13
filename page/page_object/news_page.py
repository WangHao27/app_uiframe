# -*- coding: utf-8 -*-
"""
@Time ： 2021/3/7 15:14
@Auth ： wanghao
@File ：news_page.py
"""
import allure
from page.basepage import BasePage
from page.page_object.address_page import AddressListPage

class newsPage(BasePage):

    @allure.step("进入通讯录页面")
    def goto_address(self):
        self.parse_action("news_page.yaml", "goto_address")
        return AddressListPage(self.driver)

