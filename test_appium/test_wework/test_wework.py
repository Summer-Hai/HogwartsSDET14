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
        self.driver.back()
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
        self.driver.find_element_by_xpath("//*[@resource-id='com.tencent.wework:id/dyx' and  @text='通讯录']").click()

        self.driver.find_element_by_xpath("//*[@class='android.widget.TextView' and  @text='添加成员']").click()

        self.driver.find_element_by_xpath("//*[@class='android.widget.TextView' and @text='手动输入添加']").click()

        self.driver.find_element_by_xpath("//*[@class='android.widget.EditText' and @text='必填']").send_keys('summer')

        self.driver.find_element_by_id("com.tencent.wework:id/f1e").send_keys("13000008888")

        self.driver.find_element_by_xpath("//*[@resource-id='com.tencent.wework:id/axm' and @text='设置部门']").click()

        self.driver.find_element_by_id("com.tencent.wework:id/g09").click()

        self.driver.find_element_by_id("com.tencent.wework:id/h9w").click()

        print("添加成功")

    @allure.story("删除用户")
    def test_peopledel(self):
        # self.driver.find_element_by_xpath("//*[@resource-id='com.tencent.wework:id/dyx' and  @text='通讯录']").click()
        # 删除summer用户定位
        self.driver.find_element_by_xpath("//android.widget.ListView/android.widget.RelativeLayout[4]").click()

        self.driver.find_element_by_id("com.tencent.wework:id/h9p").click()

        self.driver.find_element_by_id("com.tencent.wework:id/b2c").click()

        self.driver.find_element_by_id("com.tencent.wework:id/e3f").click()

        self.driver.find_element_by_id("com.tencent.wework:id/bci").click()

        print("删除用户成功")
