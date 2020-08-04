'''
 -*- coding: utf-8 -*-
 @Time    : 2020/7/30 20:20
 @Author  : Summer
 @Email   : 2361157192@qq.com
 @File    : main.py
 
 '''
from time import sleep

import allure
import yaml
from appium.webdriver.common.mobileby import MobileBy

from xueqiu_app.page.base_page import BasePage
from xueqiu_app.page.market import Market


class Main(BasePage):

    def goto_market(self):
        # 伪造黑名单
        # self.find(MobileBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/post_status']").click()

        # self.find(MobileBy.XPATH, "//*[@resource-id='android:id/tabs']//*[@text='行情']").click()
        # self.set_implicitly_wait(3)
        #  ----- 下面是第二次修改-----
        # with open("../datas/step/main.yml", encoding="UTF-8") as f:
        #     steps = yaml.safe_load(f)
        # for step in steps:
        #     if "action" in step.keys():
        #         action = step["action"]
        #         if action == "click":
        #             self.find(step["by"],step["locator"]).click()
        with allure.step("进入行情"):
            self.steps("../datas/step/main.yml", "goto_market")
        return Market(self.driver)
