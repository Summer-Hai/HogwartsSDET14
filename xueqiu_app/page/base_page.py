'''
 -*- coding: utf-8 -*-
 @Time    : 2020/7/30 20:28
 @Author  : Summer
 @Email   : 2361157192@qq.com
 @File    : base_page.py
 
 '''
import json
import logging

import yaml
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

from xueqiu_app.page.handle_black import handle_black


class BasePage():
    logging.basicConfig(level=logging.INFO)

    _black_list = [
        (MobileBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/iv_close']")
    ]
    _max_err_num = 3
    _error_num = 0
    _params = {}

    def __init__(self, driver: WebDriver = None):
        if driver == None:
            logging.info("初始化driver")
        else:
            logging.info(f"获取driver， driver = {driver}")
        self.driver = driver

    # def find1(self, by, locator = None):
    #     try:
    #         # 如果找到元素就清空——error_num
    #         if locator is None:
    #             result = self.driver.find_element(*by)
    #         else:
    #             result = self.driver.find_element(by, locator)
    #         self._error_num = 0
    #         return result
    #     except Exception as e:
    #         # 如果没有找到，就进行黑名单处理
    #         if self._error_num > self._max_err_num:
    #             # 如果查找次数大于指定次数，清空error 次数并报异常
    #             self._error_num = 0
    #             raise e
    #         self._error_num += 1
    #         for ele in self._black_list:
    #             eles = self.finds(ele)
    #             if len(eles) > 0:
    #                 eles[0].click()
    #                 return self.find(by,locator)
    #         raise ValueError("元素不在黑名单中")

    # def find_black(fun):
    #     _black_list = [
    #         (MobileBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/iv_close']")
    #     ]
    #     _max_err_num = 3
    #     _error_num = 0
    #
    #     def black(self, *args, **kwargs):
    #         try:
    #             # 先执行一次，如果可以找到直接找到
    #             fun(self, *args, **kwargs)
    #         except Exception as e:
    #             # 找不到报错，进入黑名单查询
    #             if self._error_num > self._max_err_num:
    #                 # 如果查找次数大于指定次数，清空error 次数并报异常
    #                 self._error_num = 0
    #                 raise e
    #             # 每执行一次，累加一次
    #             self._error_num += 1
    #             # 循环查找黑名单的元素，找到定义的关闭功能，点击关闭
    #             for ele in _black_list:
    #                 eles = self.finds(ele)
    #                 if len(eles) > 0:
    #                     eles[0].click()
    #                     return fun(self, *args, **kwargs)
    #             raise ValueError("元素不在黑名单中")
    #         return fun(self, *args, **kwargs)
    #
    #     return black

    def screenshot(self, path):
        self.driver.save_screenshot(path)

    # 添加装饰器
    @handle_black
    def find(self, by, locator=None):
        logging.info(f"run find： by = {by}, locator = {locator}")
        if locator is None:
            result = self.driver.find_element(*by)
        else:
            result = self.driver.find_element(by, locator)
        return result

    def finds(self, by, locator=None):
        logging.info(f"run finds： by = {by}, locator = {locator}")
        if locator is None:
            return self.driver.find_elements(*by)
        else:
            return self.driver.find_elements(by, locator)

    def set_implicitly_wait(self, second):
        logging.info(f"run finds： second = {second}")
        self.driver.implicitly_wait(second)

    def steps(self, path, name):
        logging.info(f"run steps： path = {path}, name = {name}")
        with open(path, encoding="UTF-8") as f:
            steps = yaml.safe_load(f)[name]

        raw = json.dumps(steps)
        for key, value in self._params.items():
            raw = raw.replace('${' + key + '}', value)
        steps = json.loads(raw)

        for step in steps:
            if "action" in step.keys():
                action = step["action"]
                if action == "click":
                    self.find(step["by"], step["locator"]).click()
                if "send" == action:
                    self.find(step["by"], step["locator"]).send_keys(step["value"])
                if "len > 0" == action:
                    eles = self.finds(step["by"], step["locator"])
                    return len(eles) > 0

    def back(self, num=1):
        logging.info(f"run back： num = {num}")
        for i in range(num):
            self.driver.back()
