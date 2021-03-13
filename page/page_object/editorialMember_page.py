# -*- coding: utf-8 -*-
"""
@Auth ： 王浩
@File ：editorialMember_page.py
@Email：whang27@163.com
"""
import allure
from page.basepage import BasePage

class EditorialMemberPage(BasePage):

    @allure.step("编辑成员界面，删除成员")
    def deleteMember(self):
        self.parse_action('editorialMember_page.yaml', 'deleteMember')

