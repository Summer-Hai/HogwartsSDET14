'''
 -*- coding: utf-8 -*-
 @Time    : 2020/7/30 20:20
 @Author  : Summer
 @Email   : 2361157192@qq.com
 @File    : market.py
 
 '''
from appium.webdriver.common.mobileby import MobileBy

from xueqiu_app.page.base_page import BasePage
from xueqiu_app.page.search import Search


class Market(BasePage):

    def goto_serach(self):
        self.find(MobileBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/action_search']").click()
        return Search(self.driver)
