# -*- coding: utf-8 -*-
# @Author  : whl
# @File    : hero_factory.py

from py_oop.py_home_factory.police import Police
from py_oop.py_home_factory.timo import Timo

# 英雄工厂
class HeroFactory:

    def create_hero(self, name):
        if name == "Timo":
            return Timo()
        elif name == "Police":
            return Police()
        else:
            raise Exception("此英雄不在英雄工厂中")


hero_factory = HeroFactory()
timo = hero_factory.create_hero("Timo")
police = hero_factory.create_hero("Police")
timo.speak_lines()
police.speak_lines()
timo.fight(police)
