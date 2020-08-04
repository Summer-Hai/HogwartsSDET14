'''
 -*- coding: utf-8 -*-
 @Time    : 2020/7/30 20:33
 @Author  : Summer
 @Email   : 2361157192@qq.com
 @File    : test_market.py
 
 '''
from time import sleep

import allure
import pytest
import yaml
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from xueqiu_app.page.app import App


class TestMarket():

    def setup(self):
        self.app = App()

    def teardown(self):
        self.app.stop()

    @allure.story("搜索功能")
    def test_market(self):
        self.app.start().goto_main().goto_market()

    def load_data(self):
        with open("../datas/case/test_market.yml", encoding="utf-8") as f:
            result = yaml.safe_load(f)
        return result

    @allure.story("搜索和关注")
    @pytest.mark.parametrize("stock_name", load_data(0))
    def test_search(self, stock_name):
        search = self.app.start().goto_main().goto_market().goto_serach()
        search.search(stock_name)
        assert search.is_choose(stock_name)
        with allure.step("搜索关注成功"):
            sleep(5)
        search.back(1)
