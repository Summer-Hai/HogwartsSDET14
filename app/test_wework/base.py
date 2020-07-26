'''
 -*- coding: utf-8 -*-
 @Time    : 2020/7/25 23:21
 @Author  : Summer
 @Email   : 2361157192@qq.com
 @File    : base.py
 
 '''
from appium import webdriver
from appium.webdriver.webdriver import WebDriver


class Base():
    _driver = None

    def __init__(self, driver: WebDriver = None):

        if driver == None:
            caps = {}
            caps["platformName"] = "Android"
            caps["deviceName"] = "emulator-5554"
            caps["appPackage"] = "com.tencent.wework"
            caps["appActivity"] = ".launch.WwMainActivity"
            caps["noReset"] = "true"
            caps["dontStopAppOnReset"] = "true"
            caps["skipDeviceInitialization"] = "true"
            caps["unicodeKeyBoard"] = "true"
            self._driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
            self._driver.implicitly_wait(15)


        else:
            self._driver = driver
            self._driver.implicitly_wait(15)

    def find(self, by, locator):
        return self._driver.find_element(by, locator)
