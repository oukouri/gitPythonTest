# -*- coding: utf-8 -*-
# @Author  : whl
# @File    : test_add_department.py
import pytest

from py_selenium.page.main_page import MainPage


class TestAddDepartment:
    def setup_class(self):
        self.main = MainPage()
        self.driver = self.main.driver

    @pytest.mark.parametrize("name", ["测试部门"])
    def test_add_department(self, name):
        """
        用来测试添加部门功能
        1、主页面跳转到添加成员页面 2、添加部门 3、获取部门列表，做断言验证
        :return:
        """
        dep_list = self.main.goto_add_member().goto_add_department().add_department(name).get_dep_list()
        print('dep_list:', dep_list)
        # rjust，向右对齐，在左边补空格
        assert name.rjust(len(name) + 1) in dep_list
