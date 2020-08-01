'''
 -*- coding: utf-8 -*-
 @Time    : 2020/7/30 20:20
 @Author  : Summer
 @Email   : 2361157192@qq.com
 @File    : search.py
 
 '''
from time import sleep

from appium.webdriver.common.mobileby import MobileBy

from xueqiu_app.page.base_page import BasePage


class Search(BasePage):

    def search(self, stock_name):
        sleep(5)
        self.find(MobileBy.XPATH,
                  "//*[@resource-id='com.xueqiu.android:id/search_input_text']").send_keys("阿里巴巴")
        self.find(MobileBy.XPATH,
                  "//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴-SW']").click()
        self.find(MobileBy.XPATH,
                  f"//*[contains(@resource-id,'stock_item_container')]//*[@text='{stock_name}']/../..//*[@text='加自选']").click()

    def is_choose(self, stock_name):
        eles = self.finds(MobileBy.XPATH,
                          f"//*[contains(@resource-id,'stock_item_container')]//*[@text='{stock_name}']/../..//*[@text='已添加']")
        return len(eles) > 0
