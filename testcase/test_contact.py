# -*- coding: utf-8 -*-
"""
@Auth ： 王浩
@File ：test_contact.py
@Email：whang27@163.com
"""
import allure
import pytest
import yaml
from typing import List
from page.application import App
from utils import setting

data_path = setting.TEST_DATA
class TestContact:

    @allure.story("删除成员测试")
    @pytest.mark.parametrize('names', yaml.safe_load(open(f'{data_path}/test_deleteContact.yaml', 'r', encoding='utf-8')))
    def test_deleteContact(self, names):
        name = names['name']
        steps = App().start().goto_newsPage().goto_address().goto_search()
        beforeNum: List = steps.get_membersNumber(name)
        steps.goto_personalInfo().goto_InfoSettings().goto_editorialMember().deleteMember()
        afterNum: List = steps.get_membersNumber(name)
        assert len(beforeNum) - len(afterNum) == 1


    @allure.story("添加成员测试")
    @pytest.mark.parametrize('information', yaml.safe_load(open(f'{data_path}/test_saveMembers.yaml', 'r', encoding='utf-8')))
    def test_saveMembers(self, information):
        name = information[0]
        phone = information[1]
        App().start().goto_newsPage().goto_address().goto_addmenbers().goto_savemembers().savemembers(name=name, phone=phone)
