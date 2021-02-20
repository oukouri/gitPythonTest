# -*- coding: utf-8 -*-
# @Author  : whl
# @File    : send.py
import money


# 发工资模块
def send_money(salary):
    money.saved_money += salary
    print(f"最终存款金额为{money.saved_money}")
