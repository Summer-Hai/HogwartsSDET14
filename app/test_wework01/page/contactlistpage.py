'''
 -*- coding: utf-8 -*-
 @Time    : 2020/7/27 22:24
 @Author  : Summer
 @Email   : 2361157192@qq.com
 @File    : contactlistpage.py
 通讯录列表页
 '''
import allure
from appium.webdriver.common.mobileby import MobileBy

from app.test_wework01.page.addmemberPage import AddMemberPage
from app.test_wework01.page.basepage import BasePage
from app.test_wework01.page.searchmemberpage import SearchMemberPage


class ContactListPage(BasePage):
    # def __init__(self, driver):
    #     self.driver = driver

    addmember_text = "添加成员"
    search_contact_element = (MobileBy.ID, "com.tencent.wework:id/h9z")
    def addcontact(self):
        # 添加联系人
        # self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
        #                          'new UiScrollable(new UiSelector()'
        #                          '.scrollable(true).instance(0))'
        #                          '.scrollIntoView(new UiSelector()'
        #                          '.text("添加成员").instance(0));').click()

        with allure.step("点击添加成员"):
            self.find_by_scroll(self.addmember_text).click()

        return AddMemberPage(self.driver)

    def search_contact(self):
        """
        点击搜索，进入搜索页面
        :return:
        """
        with allure.step("点击搜索，进入搜索页面"):
            self.find_and_click(self.search_contact_element)

        return SearchMemberPage(self.driver)
