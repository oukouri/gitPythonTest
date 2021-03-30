# -*- coding: utf-8 -*-
# @Author  : whl
# @File    : hero.py

# 英雄父类
class Hero:
    hp = 0
    power = 0
    name = ""

    # 战斗方法
    def fight(self, enemy):
        """
        :param enemy:敌人的变量对象
        :return:
        """
        # 我的血量
        my_hp = self.hp - enemy.power
        # 敌人血量
        enemy_hp = enemy.hp - self.power
        # 开始判断输赢
        if my_hp > enemy_hp:
            print(f"{self.name}赢了，{enemy.name}输了!")
        elif my_hp < enemy_hp:
            print(f"{enemy.name}赢了，{self.name}输了!")
        else:
            print(f"{self.name}与{enemy.name}打平手了!")

    # 台词方法
    def speak_lines(self):
        # Timo，Police台词
        if self.name == "Timo":
            print("提莫队长正在待命")
        elif self.name == "Police":
            print("见识一下法律的子弹")
        else:
            print("无台词")
