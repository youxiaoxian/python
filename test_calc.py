from decimal import Decimal

import pytest
import yaml

from python1.Calculator import Calculator


class TestCal:
    def setup_class(self):
        print("所有计算开始")
        self.calc = Calculator()

    def teardown_class(self):
        print("所有计算结束")

    def setup(self):
        print("计算开始")

    def teardown(self):
        print("计算结束")

    id = ['int', 'float', 'int&float', 'big', 'zero']

    @pytest.mark.parametrize('a,b,expect', yaml.safe_load(open("param_add.yml")), ids=id)
    def test_add(self, a, b, expect):
        assert expect == self.calc.add(a, b)

    @pytest.mark.parametrize('a,b,expect', yaml.safe_load(open("param_div.yml")), ids=id)
    def test_div(self, a, b, expect):
        assert Decimal(expect).quantize(Decimal("0.00")) == self.calc.div(a, b)
