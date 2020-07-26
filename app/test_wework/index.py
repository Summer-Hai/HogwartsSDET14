'''
 -*- coding: utf-8 -*-
 @Time    : 2020/7/25 23:21
 @Author  : Summer
 @Email   : 2361157192@qq.com
 @File    : index.py
 
 '''
from time import sleep

from appium.webdriver.common.mobileby import MobileBy

from app.test_wework.Personnel import Personnel
from app.test_wework.base import Base


class Index(Base):

    def get_address_list(self):
        sleep(10)
        self.find(MobileBy.XPATH, "//*[@text='通讯录']").click()

        return Personnel(self._driver)
