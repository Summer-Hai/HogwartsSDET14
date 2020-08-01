'''
 -*- coding: utf-8 -*-
 @Time    : 2020/7/30 20:33
 @Author  : Summer
 @Email   : 2361157192@qq.com
 @File    : test_market.py
 
 '''
from time import sleep

from xueqiu_app.page.app import App


class TestMarket():

    def setup(self):
        self.app = App()

    def teardown(self):
        self.app.stop()

    def test_market(self):
        self.app.start().goto_main().goto_market()

    def test_search(self):
        search = self.app.start().goto_main().goto_market().goto_serach()
        search.search("阿里巴巴-SW")
        assert search.is_choose("阿里巴巴-SW")
        sleep(5)
