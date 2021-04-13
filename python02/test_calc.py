from decimal import Decimal

import allure
import pytest

import pytest_ordering


@allure.feature("计算器")
class TestCal:

    # @pytest.mark.second
    @pytest.mark.run(order=2)
    @allure.story("整数相加")
    def test_add_int(self, get_add_int_param_calc, inicalc_class):
        assert get_add_int_param_calc[2] == inicalc_class.add(get_add_int_param_calc[0], get_add_int_param_calc[1])

    @pytest.mark.run(order=1)
    # @pytest.mark.first
    @allure.story("小数相加")
    def test_add_float(self, get_add_float_param_calc, inicalc_class):
        assert get_add_float_param_calc[2] == round(
            inicalc_class.add(get_add_float_param_calc[0], get_add_float_param_calc[1]), 2)

    @allure.story("整数相除")
    @pytest.mark.run(order=3)
    def test_div_int(self, get_div_int_param_calc, inicalc_class):
        try:
            assert Decimal(get_div_int_param_calc[2]).quantize(Decimal("0.00")) == Decimal(
                inicalc_class.div(get_div_int_param_calc[0], get_div_int_param_calc[1])).quantize(Decimal("0.00"))
        except ZeroDivisionError:
            print('ZeroDivisionError')

    # @pytest.mark.last
    @pytest.mark.run(order=-1)
    @allure.story("小数相除")
    def test_div_float(self, get_div_float_param_calc, inicalc_class):
        try:
            assert Decimal(get_div_float_param_calc[2]).quantize(Decimal("0.00")) == Decimal(
                inicalc_class.div(get_div_float_param_calc[0], get_div_float_param_calc[1])).quantize(Decimal("0.00"))
        except ZeroDivisionError:
            print('ZeroDivisionError')
