# -*- coding: utf-8 -*-
"""
@Auth ： 王浩
@File ：infoSettings_page.py
@Email：whang27@163.com
"""
import allure
from page.basepage import BasePage
from page.page_object.editorialMember_page import EditorialMemberPage

class InfoSettingsPage(BasePage):

    @allure.step("进入编辑成员页面")
    def goto_editorialMember(self):
        self.parse_action('infoSettings_page.yaml', 'goto_editorialMember')
        return  EditorialMemberPage(self.driver)