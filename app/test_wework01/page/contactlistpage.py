'''
 -*- coding: utf-8 -*-
 @Time    : 2020/7/27 22:24
 @Author  : Summer
 @Email   : 2361157192@qq.com
 @File    : contactlistpage.py
 通讯录列表页
 '''
from appium.webdriver.common.mobileby import MobileBy

from app.test_wework01.page.addmemberPage import AddMemberPage
from app.test_wework01.page.basepage import BasePage


class ContactListPage(BasePage):
    # def __init__(self, driver):
    #     self.driver = driver

    addmember_text = "添加成员"

    def addcontact(self):
        # 添加联系人
        # self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
        #                          'new UiScrollable(new UiSelector()'
        #                          '.scrollable(true).instance(0))'
        #                          '.scrollIntoView(new UiSelector()'
        #                          '.text("添加成员").instance(0));').click()

        self.find_by_scroll(self.addmember_text).click()

        return AddMemberPage(self.driver)

    def search_contact(self):
        pass
