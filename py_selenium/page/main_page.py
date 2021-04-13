# -*- coding: utf-8 -*-
# @Author  : whl
# @File    : main_page.py
from selenium.webdriver.common.by import By

from py_selenium.page.add_member_page import AddMemberPage
from py_selenium.page.base_page import BasePage


class MainPage(BasePage):
    # 元素定位封装成了一个元祖
    add_member_ele = (By.CSS_SELECTOR, ".ww_indexImg_AddMember")

    def goto_add_member(self):
        self.find(self.add_member_ele).click()
        return AddMemberPage(self.driver)
