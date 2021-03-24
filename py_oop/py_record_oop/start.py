# -*- coding: utf-8 -*-
# @Author  : whl
# @File    : start.py
from py_oop.py_record_oop.send import send_money
from py_oop.py_record_oop.select import select_money

if __name__ == '__main__':
    send_money(select_money(1000))