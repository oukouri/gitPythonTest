# -*- coding: utf-8 -*-
# @Author  : whl
# @File    : test_calc.py
import pytest
from py_pytest.pytest_test.base import TestBase


class TestCalc(TestBase):

    # 加法测试
    @pytest.mark.parametrize(
        "a, b, expect",
        TestBase.get_datas("add")["datas"], ids=TestBase.get_datas("add")["ids"]
    )
    @pytest.mark.add
    def test_add(self, a, b, expect):
        # 定义一个变量接收add方法的返回值
        # 调用相加方法
        result = self.calc.add(a, b)
        if isinstance(result, float):
            result = round(result, 2)
        # 得到相加结果之后写断言
        assert result == expect

    # 减法测试
    @pytest.mark.parametrize(
        "a, b, expect",
        TestBase.get_datas("sub")["datas"], ids=TestBase.get_datas("sub")["ids"]
    )
    @pytest.mark.sub
    def test_sub(self, a, b, expect):
        # 定义一个变量接收sub方法的返回值
        # 调用相减方法
        result = self.calc.sub(a, b)
        if isinstance(result, float):
            result = round(result, 2)
        # 得到相减结果之后写断言
        assert result == expect

    # 乘法测试
    @pytest.mark.parametrize(
        "a,b,expect",
        TestBase.get_datas("mul")["datas"], ids=TestBase.get_datas("mul")["ids"]
    )
    @pytest.mark.mul
    def test_mul(self, a, b, expect):
        # 定义一个变量接收mul方法的返回值
        # 调用相乘方法
        result = self.calc.mul(a, b)
        if isinstance(result, float):
            result = round(result, 2)
        # 得到相乘结果之后写断言
        assert result == expect

    # 除法测试
    @pytest.mark.parametrize(
        "a,b,expect",
        TestBase.get_datas("div")["datas"], ids=TestBase.get_datas("div")["ids"]
    )
    @pytest.mark.div
    def test_div(self, a, b, expect):
        # 定义一个变量接收div方法的返回值
        # 调用相除方法
        if b == 0:
            with pytest.raises(ZeroDivisionError):
                self.calc.div(a, b)
        else:
            result = self.calc.div(a, b)
            if isinstance(result, float):
                result = round(result, 2)
            # 得到相除结果之后写断言
            assert result == expect
