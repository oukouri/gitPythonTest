# -*- coding: utf-8 -*-
# @Author  : whl
# @File    : cat.py
# 动物子类
from python_home_oop.animal import Animal


class Cat(Animal):
    # 重写父类的__init__方法，继承父类的属性
    def __init__(self, name, color, age, sex):
        super().__init__(name, color, age, sex)
        # 添加一个新的属性，毛发 = 短毛
        self.hair = "短毛"

    # 会捉老鼠方法
    def catch_mouse(self):
        print(f"我是{self.name},会捉老鼠")

    # 改写父类会叫方法
    def call(self):
        print(f"我是{self.name},喵喵叫")


if __name__ == '__main__':
    cat_m = Cat('miaomiao', 'Yellow', 4, 'M')
    cat_m.catch_mouse()
    cat_m.call()
    cat_m.run()
    print(f"我是{cat_m.name},毛发是{cat_m.hair}")