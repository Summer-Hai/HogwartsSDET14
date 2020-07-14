'''
 -*- coding: utf-8 -*-
 @Time    : 2020/7/12 15:25
 @Author  : Summer
 @Email   : 2361157192@qq.com
 @File    : check_demo.py
 
 '''
import yaml


def get_steps():
    with open("../steps/ufunc,yml") as f:
        datas = yaml.safe_load(f)
        return datas


def steps(a, b, result):
    steps1 = get_steps()

    for step in steps1:
        if 'add' == step:
            assert a + b == result


def check_demo():
    print("111")


class CheckDemo():

    def check_demo1(self):
        print("2222")
