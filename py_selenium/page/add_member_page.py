# -*- coding: utf-8 -*-
# @Author  : whl
# @File    : add_member_page.py
from selenium.webdriver.common.by import By

from py_selenium.page.add_department_page import AddDepartmentPage
from py_selenium.page.base_page import BasePage
from py_selenium.page.contact_page import ContactPage


class AddMemberPage(BasePage):
    # 姓名
    add_user_name = (By.ID, "username")
    # 账号
    add_memberAdd_acctid = (By.ID, "memberAdd_acctid")
    # 手机号
    add_memberAdd_phone = (By.ID, "memberAdd_phone")

    def add_member(self, name):
        # 添加姓名、 账号、 手机号
        self.find(self.add_user_name).send_keys(name)
        self.find(self.add_memberAdd_acctid).send_keys("111")
        self.find(self.add_memberAdd_phone).send_keys("13199991111")
        # 点击保存
        self.driver.find_element(By.CSS_SELECTOR, ".qui_btn.ww_btn.js_btn_save").click()
        return ContactPage(self.driver)

    def goto_add_department(self):
        # 点击添加部门
        self.driver.find_element(By.XPATH, '//*[@class="member_colLeft_top_addBtn"]').click()
        self.driver.find_element(By.CSS_SELECTOR, ".js_create_party").click()
        return AddDepartmentPage(self.driver)
