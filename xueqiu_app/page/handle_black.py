'''
 -*- coding: utf-8 -*-
 @Time    : 2020/8/2 21:21
 @Author  : Summer
 @Email   : 2361157192@qq.com
 @File    : handle_black.py
 
 '''
import logging

import allure
from appium.webdriver.common.mobileby import MobileBy


def handle_black(func):
    logging.basicConfig(level=logging.INFO)

    def wrapper(*args, **kwargs):
        _black_list = [
            (MobileBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/iv_close']")
        ]
        from xueqiu_app.page.base_page import BasePage
        instance: BasePage = args[0]
        try:
            logging.info("run" + func.__name__ + "\n args: " + repr(args[1:]) + "\n" + repr(kwargs))
            element = func(*args, **kwargs)
            _error_num = 0
            instance.set_implicitly_wait(3)
            return element
        except Exception as e:
            instance.screenshot("tmp.png")
            with open("tmp.png", "rb") as f:
                content = f.read()
            allure.attach(content, attachment_type=allure.attachment_type.PNG)
            logging.error("element not found, handle black list")
            instance.set_implicitly_wait(1)
            # 如果没有找到，就进行黑名单处理
            if instance._error_num > instance._max_err_num:
                # 如果查找次数大于指定次数，清空error 次数并报异常
                instance._error_num = 0
                raise e
            instance._error_num += 1
            for ele in instance._black_list:
                eles = instance.finds(ele)
                if len(eles) > 0:
                    eles[0].click()
                    return wrapper(*args, **kwargs)
            raise ValueError("元素不在黑名单中")

    return wrapper
