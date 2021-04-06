# -*- coding: utf-8 -*-
# @Author  : whl
# @File    : base.py
import yaml

from py_pytest.python_code.calc import Calculator


class TestBase:
    def setup_class(self):
        print("开始计算")
        # 实例化计算器类
        self.calc = Calculator()

    def teardown_class(self):
        print("结束计算")

    @classmethod
    def get_datas(cls, dataflag):
        """
        :param dataflag: yaml文件中的测试数据标记 add-加法
        :return:
        """
        with open("../datas/calc_datas.yaml") as f:
            datas = yaml.safe_load(f)[dataflag]
            testdatas = datas["datas"]
            myid = datas["myid"]
            print(myid)
            return {"datas": testdatas, "ids": myid}
