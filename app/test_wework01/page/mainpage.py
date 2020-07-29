'''
 -*- coding: utf-8 -*-
 @Time    : 2020/7/27 22:22
 @Author  : Summer
 @Email   : 2361157192@qq.com
 @File    : mainpage.py

 主页面
 '''
import allure
from appium.webdriver.common.mobileby import MobileBy

from app.test_wework01.page.basepage import BasePage
from app.test_wework01.page.contactlistpage import ContactListPage


class MainPage(BasePage):
    # def __init__(self,driver):
    #    self.driver = driver

    contactlist = (MobileBy.XPATH, "//android.widget.TextView[@text='通讯录']")

    def goto_contactlist(self):
        """
        进入到通讯录
        """
        # self.driver.find_element(MobileBy.XPATH, "//android.widget.TextView[@text='通讯录']").click()
        with allure.step("点击通讯录"):
            self.find_and_click(self.contactlist)

        return ContactListPage(self.driver)

    def goto_workbench(self):
        pass
