'''
 -*- coding: utf-8 -*-
 @Time    : 2020/7/25 23:25
 @Author  : Summer
 @Email   : 2361157192@qq.com
 @File    : test_run.py
 
 '''
import allure

from app.test_wework.index import Index


class TestPersonnel():

    def setup(self):
        self.index = Index()
        self.username = "summer"

    @allure.story("添加用户")
    def test_add_user(self):
        self.index.get_address_list().add_user(self.username)

    @allure.story("删除用户")
    def test_del_user(self):
        self.index.get_address_list().del_user(self.username)
