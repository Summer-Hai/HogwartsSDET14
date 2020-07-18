'''
 -*- coding: utf-8 -*-
 @Time    : 2020/7/17 22:32
 @Author  : Summer
 @Email   : 2361157192@qq.com
 @File    : test_window.py
 
 '''
from selenium import webdriver
from testing.base import Base
import time


class TestWindows(Base):

    def test_window(self):
        self.driver.get("http://www.baidu.com")
        self.driver.find_element_by_link_text("登录").click()
        self.driver.find_element_by_link_text("立即注册").click()
        print(self.driver.current_window_handle)
        print(self.driver.window_handles)
        window = self.driver.window_handles
        self.driver.switch_to_window(window[1])
        self.driver.find_element_by_id("TANGRAM__PSP_4__userName").send_keys("username")
        self.driver.find_element_by_id("TANGRAM__PSP_4__phone").send_keys("15119919675")
        time.sleep(5)
        self.driver.switch_to_window(window[0])
        self.driver.find_element_by_id("TANGRAM__PSP_11__footerULoginBtn").click()

        self.driver.find_element_by_id("TANGRAM__PSP_11__userName").send_keys("login_name")
        self.driver.find_element_by_id("TANGRAM__PSP_11__password").send_keys("login_password")

        self.driver.find_element_by_id("TANGRAM__PSP_11__submit").click()
        time.sleep(6)
