# -*- coding: utf-8 -*-
# @Author  : whl
# @File    : animal.py
# 动物类
class Animal:
    def __init__(self, name, color, age, sex):
        # 初始化属性
        self.name = name
        self.color = color
        self.age = age
        self.sex = sex

    # 会叫方法
    def call(self):
        print(f"我是{self.name}会叫")

    # 会跑方法
    def run(self):
        print(f"我是{self.name}会跑")


if __name__ == '__main__':
    panda = Animal('panda', 'BLACK', 3, 'F')
    panda.call()
    panda.run()