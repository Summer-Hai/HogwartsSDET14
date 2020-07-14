'''
 -*- coding: utf-8 -*-
 @Time    : 2020/7/12 16:50
 @Author  : Summer
 @Email   : 2361157192@qq.com
 @File    : test_ven.py
 
 '''


# 测试用例通过传入fixture方法，获取 测试数据/开发数据
def test_case(cmdoption):
    print("测试环境")
    env, datas = cmdoption
    print(f"环境：{env},数据：{datas}")
    print(f"https://{datas['env']['ip']}:{datas['env']['port']}")
