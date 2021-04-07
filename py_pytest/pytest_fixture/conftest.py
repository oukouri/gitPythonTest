# -*- coding: utf-8 -*-
# @Author  : whl
# @File    : conftest.py
import pytest
import yaml
from py_pytest.python_code.calc import Calculator

# 加载测试数据文件
with open("../datas/calc_datas.yaml") as f:
    test_data = yaml.safe_load(f)

# 获取加法的测试数据和ids
add_datas = test_data["add"]["datas"]
add_ids = test_data["add"]["myid"]


# 相加进行fixture参数化
@pytest.fixture(scope="class", params=add_datas, ids=add_ids)
def get_add_datas(request):
    print('开始计算')
    add_data = request.param
    print(f"相加测试数据为：{add_data}")
    yield add_data
    print("结束计算")


# 获取相除的测试数据和ids
div_datas = test_data["div"]["datas"]
div_ids = test_data["div"]["myid"]


# 相除进行fixture参数化
@pytest.fixture(scope='class', params=div_datas, ids=div_ids)
def get_div_datas(request):
    print("开始计算")
    div_data = request.param
    print(f"相除测试数据为：{div_data}")
    yield div_data
    print("结束计算")


# 获取计算器实例
@pytest.fixture(scope='class')
def get_calc():
    print("获取计算器实例")
    calc = Calculator()
    return calc
