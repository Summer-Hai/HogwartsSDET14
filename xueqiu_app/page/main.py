'''
 -*- coding: utf-8 -*-
 @Time    : 2020/7/30 20:20
 @Author  : Summer
 @Email   : 2361157192@qq.com
 @File    : main.py
 
 '''
from time import sleep

from appium.webdriver.common.mobileby import MobileBy

from xueqiu_app.page.base_page import BasePage
from xueqiu_app.page.market import Market


class Main(BasePage):

    def goto_market(self):
        # 伪造黑名单
        sleep(5)
        self.find(MobileBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/post_status']").click()
        sleep(5)
        self.find(MobileBy.XPATH, "//*[@resource-id='android:id/tabs']//*[@text='行情']").click()
        self.set_implicitly_wait(3)
        return Market(self.driver)
