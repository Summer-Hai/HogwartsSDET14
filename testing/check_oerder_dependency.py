'''
 -*- coding: utf-8 -*-
 @Time    : 2020/7/14 7:26
 @Author  : Summer
 @Email   : 2361157192@qq.com
 @File    : check_oerder_dependency.py
 
 '''
'''
 -*- coding: utf-8 -*-
 @Time    : 2020/7/13 20:52
 @Author  : Summer
 @Email   : 2361157192@qq.com
 @File    : check_calc.py

 '''
import pytest
import yaml

from pythoncode.calc import Calculator

with open("../datas/calc1.yml") as f:
    datas = yaml.safe_load(f)

    adddatas = datas['add'].values()
    addids = datas['add'].keys()

    subdatas = datas['sub'].values()
    subids = datas['sub'].keys()

    muldatas = datas['mul'].values()
    mulids = datas['mul'].keys()

    divdatas = datas['div'].values()
    divids = datas['div'].keys()


class CheckCalc():

    def setup(self):
        self.cal = Calculator()

    # 加法
    @pytest.mark.first
    @pytest.mark.dependency()
    @pytest.mark.parametrize("a,b,result", adddatas, ids=addids)
    def check_add(self, a, b, result):
        print(f"\n计算数据：a={a},b={b},result={result}")
        assert self.cal.add(a, b) == result

    #除法
    @pytest.mark.last
    @pytest.mark.dependency(depends=["test_mul"])
    @pytest.mark.parametrize("a,b,result", divdatas, ids=divids)
    def check_div(self, a, b, result):
        print(f"\n计算数据：a={a},b={b},result={result}")
        assert self.cal.div(a, b) == result

    # 减法
    @pytest.mark.second
    @pytest.mark.dependency(depends=["test_add"])
    @pytest.mark.parametrize("a,b,result", subdatas, ids=subids)
    def check_sub(self, a, b, result):
        print(f"\n计算数据：a={a},b={b},result={result}")
        assert self.cal.sub(a, b) == result

    #乘法
    @pytest.mark.third
    @pytest.mark.dependency()
    @pytest.mark.parametrize("a,b,result", muldatas, ids=mulids)
    def check_mul(self, a, b, result):
        print(f"\n计算数据：a={a},b={b},result={result}")
        assert self.cal.mul(a, b) == result


if __name__ == '__main__':
    pytest.main(['check_order_pendency.py', '-v', '-s'])
