'''
 -*- coding: utf-8 -*-
 @Time    : 2020/7/28 22:13
 @Author  : Summer
 @Email   : 2361157192@qq.com
 @File    : basepage.py
 '''
import logging

from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

"""
BasePage:存放一些基本的方法，比如：初始化 driver
"""


class BasePage:
    logging.basicConfig(level=logging.INFO)

    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def find(self, locator):
        logging.info(f"find:{locator}")
        return self.driver.find_element(*locator)

    def finds(self, locator):
        logging.info(f"finds:{locator}")
        return self.driver.find_elements(*locator)

    def find_and_click(self, locator):
        logging.info(f"find_and_click:{locator}")
        return self.driver.find_element(*locator).click()

    def find_and_sendkeys(self, locator, text):
        logging.info(f"find_and_sendkeys:{locator},{text}")
        return self.driver.find_element(*locator).send_keys(text)

    def find_by_scroll(self, text):
        logging.info(f"find_by_scroll:{text}")
        return self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                        'new UiScrollable(new UiSelector()'
                                        '.scrollable(true).instance(0))'
                                        '.scrollIntoView(new UiSelector()'
                                        f'.text("{text}").instance(0));')

    def webdriver_wait(self, locator, timeout=10):
        logging.info(f"webdriver_wait:{locator},{timeout}")
        element = WebDriverWait(self.driver, timeout).until(
            lambda x: x.find_element(*locator))
        return element

    def back(self, num=1):
        logging.info(f"back:{num}")
        for i in range(num):
            self.driver.back()
