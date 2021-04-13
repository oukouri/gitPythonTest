# -*- coding: utf-8 -*-
# @Author  : whl
# @File    : contact_page.py
from selenium.webdriver.common.by import By

from py_selenium.page.base_page import BasePage


class ContactPage(BasePage):

    def goto_add_member(self):
        pass

    def get_list(self):
        #
        ele_list = self.driver.find_elements(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
        name_list = [i.text for i in ele_list]
        # name_list = []
        # for i in ele_list:
        #     name_list.append(i.text)
        # print(name_list)
        return name_list

    def get_dep_list(self):
        # 获取部门列表
        ele_dep_list = self.driver.find_elements(By.CSS_SELECTOR, ".jstree-node.js_editable.jstree-leaf")
        dep_list = [i.text for i in ele_dep_list]
        return dep_list
