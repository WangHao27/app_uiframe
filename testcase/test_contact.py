# -*- coding: utf-8 -*-
"""
@Auth ： 王浩
@File ：test_contact.py
@Email：whang27@163.com
"""
import json
import os
from typing import List, Dict

import allure
import pytest
import yaml
from page.application import App
from utils import setting

data_path = setting.TEST_DATA
class TestContact:

    @allure.story("删除成员测试")
    @pytest.mark.parametrize('names', yaml.safe_load(open(f'{data_path}/test_deleteContact.yaml', 'r', encoding='utf-8')))
    def test_deleteContact(self, names):
        name = names['name']
        App().start().goto_newsPage().goto_address().goto_personalInfo(name).goto_InfoSettings().goto_editorialMember().deleteMember()

    @allure.story("添加成员测试")
    @pytest.mark.parametrize('information', yaml.safe_load(open(f'{data_path}/test_saveMembers.yaml', 'r', encoding='utf-8')))
    def test_saveMembers(self, information):
        name = information[0]
        phone = information[1]
        App().start().goto_newsPage().goto_address().goto_addmenbers().goto_savemembers().savemembers(name=name, phone=phone)