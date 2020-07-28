'''
 -*- coding: utf-8 -*-
 @Time    : 2020/7/27 22:31
 @Author  : Summer
 @Email   : 2361157192@qq.com
 @File    : contactaddpage.py
 
 '''
from appium.webdriver.common.mobileby import MobileBy

from app.test_wework01.page.basepage import BasePage


class ContactAddPage(BasePage):
    # def __init__(self, driver):
    #     self.driver = driver

    name_element = (MobileBy.XPATH,
                    "//*[contains(@text,'姓名')]/../android.widget.EditText")
    gender_element = (MobileBy.XPATH, "//*[contains(@text,'性别')]/..//*[@text='男']")
    male_ele = (MobileBy.XPATH, "//*[@text='男']")
    female_ele = (MobileBy.XPATH, "//*[@text='女']")
    phonenum_element = (MobileBy.XPATH, "//*[contains(@text,'手机号')]")
    save_element = (MobileBy.ID, "com.tencent.wework:id/h9w")

    def set_name(self, name):
        # 设置姓名
        # self.driver.find_element(MobileBy.XPATH,
        #                          "//*[contains(@text,'姓名')]/../android.widget.EditText").send_keys(name)
        self.find_and_sendkeys(self.name_element, name)

        return self

    def set_gender(self, gender):
        # 设置性别
        # self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'性别')]/..//*[@text='男']").click()
        # if gender == '男':
        #     self.driver.find_element(MobileBy.XPATH, "//*[@text='男']").click()
        # else:
        #     self.driver.find_element(MobileBy.XPATH, "//*[@text='女']").click()
        self.find_and_click(self.gender_element)

        if gender == '男':
            self.find_and_click(self.male_ele)
        else:
            self.find_and_click(self.female_ele)

        return self

    def set_phonenum(self, phonenum):

        # 设置手机号
        # self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'手机号')]").send_keys(phonenum)
        self.find_and_sendkeys(self.phonenum_element, phonenum)
        return self

    def click_save(self):

        # 点击保存
        # self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/h9w").click()
        self.find_and_click(self.save_element)
        from app.test_wework01.page.addmemberPage import AddMemberPage
        return AddMemberPage(self.driver)
