'''
 -*- coding: utf-8 -*-
 @Time    : 2020/7/27 22:29
 @Author  : Summer
 @Email   : 2361157192@qq.com
 @File    : addmemberPage.py

 手动添加成员页
 '''
# from app.test_wework01.page.contactaddpage import ContactAddPage
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait

from app.test_wework01.page.basepage import BasePage


class AddMemberPage(BasePage):
    # def __init__(self, driver):
    #     self.driver = driver

    add_menual_element = (MobileBy.XPATH,
                          "//android.widget.TextView[@text='手动输入添加']")
    toast_element = (MobileBy.XPATH, "//*[@class='android.widget.Toast']")

    def add_menual(self):
        """
        手动输入添加成员

        """
        # self.driver.find_element(MobileBy.XPATH,
        #                          "//android.widget.TextView[@text='手动输入添加']").click()

        self.find_and_click(self.add_menual_element)
        from app.test_wework01.page.contactaddpage import ContactAddPage
        return ContactAddPage(self.driver)

    def get_toast(self):
        element = self.webdriver_wait(self.toast_element)

        result = element.text
        # text = "成功"
        return result
