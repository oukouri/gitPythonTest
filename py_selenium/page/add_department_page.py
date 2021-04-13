# -*- coding: utf-8 -*-
# @Author  : whl
# @File    : add_department_page.py
from time import sleep

from selenium.webdriver.common.by import By

from py_selenium.page.base_page import BasePage
from py_selenium.page.contact_page import ContactPage


class AddDepartmentPage(BasePage):
    def add_department(self, name):
        # self.driver.find_element(By.NAME, "name").send_keys(name)
        # 部门名称
        self.driver.find_element(By.CSS_SELECTOR, '[name=name]').send_keys(name)
        # 选择所属部门
        self.driver.find_element(By.CSS_SELECTOR, ".js_parent_party_name").click()
        self.driver.find_element(By.CSS_SELECTOR, ".qui_dialog_body.ww_dialog_body [id='1688850436043722_anchor']").click()
        self.driver.find_element(By.CSS_SELECTOR, "[id=__dialog__MNDialog__] div>div>a:nth-child(1)").click()
        sleep(3)
        return ContactPage(self.driver)
