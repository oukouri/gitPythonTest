# -*- coding: utf-8 -*-
# @Author  : whl
# @File    : test_calc_new.py
import allure
import pytest


@allure.feature("测试计算器")
class TestCalc:
    # 相加测试用例
    @allure.story("测试加法")
    @pytest.mark.add
    def test_add(self, get_calc, get_add_datas):
        # 调用相加方法
        with allure.step("计算两个数的相加和"):
            result = get_calc.add(get_add_datas[0], get_add_datas[1])
        if isinstance(result, float):
            result = round(result, 2)
        # 得到相加结果之后写断言
        assert result == get_add_datas[2]

    @allure.story("测试除法")
    @pytest.mark.div
    def test_div(self, get_calc, get_div_datas):
        # 调用相除方法
        with allure.step("计算两个数的相除"):
            if get_div_datas[1] == 0:
                with pytest.raises(ZeroDivisionError):
                    get_calc.div(get_div_datas[0], get_div_datas[1])
            else:
                result = get_calc.div(get_div_datas[0], get_div_datas[1])
                if isinstance(result, float):
                    result = round(result, 2)
                # 得到相除结果之后写断言
                assert result == get_div_datas[2]
