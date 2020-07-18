'''
 -*- coding: utf-8 -*-
 @Time    : 2020/7/15 21:28
 @Author  : Summer
 @Email   : 2361157192@qq.com
 @File    : test_selenium.py
 
 '''
from selenium import webdriver
from time import sleep


class TestSelenium:

    def setup(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://www.baidu.com")
        sleep(4)

    def teardown(self):
        self.driver.quit()

    def test_selenium(self):
        pass
