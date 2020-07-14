import pytest
import yaml, sys, os
from pythoncode.calc import Calculator

sys.path.append(os.path.abspath('../..'))


class TestCalc1():
    def setup(self):
        self.cal = Calculator()

    @pytest.mark.add
    @pytest.mark.parametrize(('a', 'b', 'result'), yaml.safe_load(open(r'../datas/calc.yml'))['add'])
    def test_add(self, a, b, result, open1):
        print(f"计算数据：  a={a}, b={b}, result={result}")
        assert self.cal.add(a, b) == result

    @pytest.mark.div
    @pytest.mark.parametrize(('a', 'b', 'result'), yaml.safe_load(open(r'../datas/calc.yml'))['div'])
    def test_div(self, a, b, result, open1):
        print(f"计算数据：  a={a}, b={b}, result={result}")
        assert self.cal.div(a, b) == result

    @pytest.mark.mul
    @pytest.mark.parametrize(('a', 'b', 'result'), yaml.safe_load(open(r'../datas/calc.yml'))['mul'])
    def test_mul(self, a, b, result, open1):
        print(f"计算数据：  a={a}, b={b}, result={result}")
        assert self.cal.mul(a, b) == result

    @pytest.mark.sub
    @pytest.mark.parametrize(('a', 'b', 'result'), yaml.safe_load(open(r'../datas/calc.yml'))['sub'])
    def test_sub(self, a, b, result, open1):
        print(f"计算数据： a={a}, b={b}, result={result}")
        assert self.cal.sub(a, b) == result
