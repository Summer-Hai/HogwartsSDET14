'''
 -*- coding: utf-8 -*-
 @Time    : 2020/7/23 22:38
 @Author  : Summer
 @Email   : 2361157192@qq.com
 @File    : test_wework.py

 '''
from time import sleep

import allure
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


class TestWework:

    def setup(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "emulator-5554"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.WwMainActivity"
        caps["noReset"] = "true"
        caps["dontStopAppOnReset"] = "true"
        caps["skipDeviceInitialization"] = "true"
        caps["unicodeKeyBoard"] = "true"
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(15)

    def teardown(self):
        # self.driver.back()
        self.driver.quit()

    @allure.story("打卡")
    def test_clockin(self):
        self.driver.find_element_by_xpath("//*[@resource-id='com.tencent.wework:id/dyx' and @text='工作台']").click()
        sleep(3)
        action = TouchAction(self.driver)
        window_rect = self.driver.get_window_rect()
        width = window_rect['width']
        height = window_rect['height']
        x = int(width / 2)
        y_start = int(height * 4 / 5)
        y_end = int(height * 1 / 5)
        action.press(x=x, y=y_start).wait(200).move_to(x=x, y=y_end).release().perform()
        self.driver.find_element_by_xpath("//*[@resource-id='com.tencent.wework:id/el8' and @text='打卡']").click()
        sleep(3)
        self.driver.find_element_by_id("com.tencent.wework:id/gw8").click()
        sleep(3)
        self.driver.find_element_by_xpath("//*[@resource-id='com.tencent.wework:id/ao_']").click()

    @allure.story("添加用户")
    def test_addpeople(self):
        # 点击通讯录进入用户列表
        with allure.step("点击通讯录"):
            self.driver.find_element_by_xpath("//*[@resource-id='com.tencent.wework:id/dyx' and  @text='通讯录']").click()
        # 点击添加成员
        with allure.step("点击添加成员"):
            self.driver.find_element_by_xpath("//*[@class='android.widget.TextView' and  @text='添加成员']").click()
        # 点击手动输入添加
        with allure.step("点击手动输入添加"):
            self.driver.find_element_by_xpath("//*[@class='android.widget.TextView' and @text='手动输入添加']").click()
        # 点击名称输入框进行姓名设置summer
        with allure.step("点击姓名输入框进行输入添加"):
            self.driver.find_element_by_xpath("//*[@class='android.widget.EditText' and @text='必填']").send_keys(
                'summer')
        # 点击手机号码输入手机号码：13000008888
        with allure.step("点击手机号码输入框点击输入13000008888"):
            self.driver.find_element_by_id("com.tencent.wework:id/f1e").send_keys("13000008888")
        # 点击设置部门进入部门设置界面
        with allure.step("点击设置部门"):
            self.driver.find_element_by_xpath("//*[@resource-id='com.tencent.wework:id/axm' and @text='设置部门']").click()
        # 点击部门确定
        with allure.step("点击点击确定功能"):
            self.driver.find_element_by_id("com.tencent.wework:id/g09").click()
        # 点击弹窗进行点击确定功能
        with allure.step("点击弹窗的确定功能"):
            self.driver.find_element_by_id("com.tencent.wework:id/h9w").click()

        sleep(5)
        # 点击返回用户列表
        with allure.step("点击返回用户列表"):
            self.driver.find_element_by_id("com.tencent.wework:id/h9e").click()

        # 添加成功
        with allure.step("添加成功"):
            print("添加成功")

    @allure.story("删除用户")
    def test_peopledel(self):
        # sleep(5)
        # with allure.step("点击通讯录"):
        #     self.driver.find_element_by_xpath("//*[@resource-id='com.tencent.wework:id/dyx' and  @text='通讯录']").click()

        # 删除summer用户定位   android.widget.ListView
        with allure.step("点击summer用户"):
            self.driver.find_element_by_xpath("//android.widget.ListView/android.widget.RelativeLayout[4]").click()

        # 点击更多功能
        with allure.step("点击更多功能"):
            self.driver.find_element_by_id("com.tencent.wework:id/h9p").click()

        # 点击用户编辑功能
        with allure.step("点击用户编辑功能"):
            self.driver.find_element_by_id("com.tencent.wework:id/b2c").click()

        # 点击删除用户功能
        with allure.step("点击删除用户功能"):
            self.driver.find_element_by_id("com.tencent.wework:id/e3f").click()

        # 点击弹窗确定功能
        with allure.step("点击弹窗确定功能"):
            self.driver.find_element_by_id("com.tencent.wework:id/bci").click()

        # 删除成功
        with allure.step("删除成功"):
            print("删除用户成功")
