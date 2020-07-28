'''
 -*- coding: utf-8 -*-
 @Time    : 2020/7/26 14:23
 @Author  : Summer
 @Email   : 2361157192@qq.com
 @File    : test_contact.py
 
 '''
from time import sleep

import pytest
import yaml
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait

'''
联系人用例
'''
with open('./datas/addcontact.yml', encoding="UTF-8") as f:
    addcontactdatas = yaml.safe_load(f)
    print(addcontactdatas)

with open('./datas/delcontact.yml', encoding="UTF-8") as f:
    delcontactdatas = yaml.safe_load(f)
    print(addcontactdatas)


class TestContact():

    def setup_class(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "emulator-5554"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.WwMainActivity"
        caps["noReset"] = "true"
        # caps["dontStopAppOnReset"] = "true"
        caps["skipDeviceInitialization"] = "true"
        caps["unicodeKeyBoard"] = "true"
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(15)

    def teardown_class(self):
        self.driver.quit()

    @pytest.mark.parametrize('name,gender,phonenum', addcontactdatas)
    def test_addcontact(self, name, gender, phonenum):
        '''
        1.打开企业微信
        2.点击通讯录
        3.点击添加成员
        4.点击手动添加
        5.输入姓名
        6.输入手机号码
        7.设置部门
        8.点击保存
        9.校验是否有添加成功的提示
        '''
        sleep(10)

        self.driver.find_element(MobileBy.XPATH, "//android.widget.TextView[@text='通讯录']").click()

        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()'
                                 '.scrollable(true).instance(0))'
                                 '.scrollIntoView(new UiSelector()'
                                 '.text("添加成员").instance(0));').click()

        self.driver.find_element(MobileBy.XPATH,
                                 "//android.widget.TextView[@text='手动输入添加']").click()
        # 设置姓名
        self.driver.find_element(MobileBy.XPATH,
                                 "//*[contains(@text,'姓名')]/../android.widget.EditText").send_keys(name)

        # 设置性别
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'性别')]/..//*[@text='男']").click()
        if gender == '男':
            self.driver.find_element(MobileBy.XPATH, "//*[@text='男']").click()
        else:
            self.driver.find_element(MobileBy.XPATH, "//*[@text='女']").click()

        # 设置手机号
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'手机号')]").send_keys(phonenum)

        # 点击保存
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/h9w").click()

        # 验证成功 Toast
        # self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        # 会报错因为Toast的时间比较短会找不到元素直接报错，需要要用到显示等待
        element = WebDriverWait(self.driver, 10).until(
            lambda x: x.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']"))

        result = element.text

        assert '成功' in result

        self.driver.back()

    @pytest.mark.parametrize('name', delcontactdatas)
    def test_delcontact(self, name):

        """
        1.打开应用
        2.点击通讯录
        3.找到要删除的联系人
        4.进入联系人页面
        5.点击右上角的三个点进入个人信息页面，点击编辑成员
        6.删除联系人
        7.确认删除
        8.验证删除成功
        """
        # name = 'summer01'

        sleep(10)
        # 2.点击通讯录
        self.driver.find_element(MobileBy.XPATH, "//android.widget.TextView[@text='通讯录']").click()
        # 3.找到要删除的联系人
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/h9z").click()

        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/fxc").send_keys(name)

        sleep(3)
        elelist = self.driver.find_elements(MobileBy.XPATH, f"//*[@text='{name}']")

        if len(elelist) < 2:
            print("没有这个联系人")
            return

        elelist[1].click()
        # 4.进入联系人页面
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/h9p").click()
        # 5.点击右上角的三个点进入个人信息页面，点击编辑成员
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/b2c").click()
        # 6.删除联系人
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/e3f").click()
        # 7.确认删除
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/bci").click()
        # 8.验证删除成功

        sleep(3)
        elelist_after = self.driver.find_elements(MobileBy.XPATH, f"//*[@text='{name}']")

        print(len(elelist), len(elelist_after))
        assert len(elelist) - len(elelist_after) == 1

        self.driver.back()
        # self.driver.back()
