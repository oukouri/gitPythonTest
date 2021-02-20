# -*- coding: utf-8 -*-
# @Author  : whl
# @File    : start.py
# 展示最终存款金额
from py_record_oop.select import select_money
from py_record_oop.send import send_money

if __name__ == '__main__':
    send_money(select_money(1000))
