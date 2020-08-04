'''
 -*- coding: utf-8 -*-
 @Time    : 2020/7/30 20:20
 @Author  : Summer
 @Email   : 2361157192@qq.com
 @File    : search.py
 
 '''
from time import sleep

import allure
import yaml
from appium.webdriver.common.mobileby import MobileBy

from xueqiu_app.page.base_page import BasePage


class Search(BasePage):

    def search(self, stock_name):
        sleep(5)
        # self.find(MobileBy.XPATH,
        #           "//*[@resource-id='com.xueqiu.android:id/search_input_text']").send_keys("阿里巴巴")
        # sleep(5)
        # self.find(MobileBy.XPATH,
        #           "//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴-SW']").click()
        # self.find(MobileBy.XPATH,
        #           f"//*[contains(@resource-id,'stock_item_container')]//*[@text='{stock_name}']/../..//*[@text='加自选']").click()
        ##### 下面是第二次修改 ######
        # with open("../datas/step/search.yml", encoding="UTF-8") as f:
        #     steps = yaml.safe_load(f)
        # for step in steps:
        #     if "action" in step.keys():
        #         action = step["action"]
        #         if action == "click":
        #             self.find(step["by"],step["locator"]).click()
        #         if "send" == action:
        #             self.find(step["by"], step["locator"]).send_keys(step["value"])
        with allure.step("进入搜索关注"):
            self._params["stock_name"] = stock_name
        self.steps("../datas/step/search.yml", "search")

    def is_choose(self, stock_name):
        # eles = self.finds(MobileBy.XPATH,
        #                   f"//*[contains(@resource-id,'stock_item_container')]//*[@text='{stock_name}']/../..//*[@text='已添加']")
        # return len(eles) > 0
        ### 下面是第二次修改#####
        # with open("../datas/step/search1.yml", encoding="UTF-8") as f:
        #     steps = yaml.safe_load(f)
        # for step in steps:
        #     if "action" in step.keys():
        #         action = step["action"]
        #         if action == "click":
        #             self.find(step["by"],step["locator"]).click()
        #         if "send" == action:
        #             self.find(step["by"], step["locator"]).send_keys(step["value"])
        #         if "len > 0" == action:
        #             eles = self.finds(step["by"], step["locator"])
        #             return len(eles) > 0
        with allure.step("校验已关注"):
            self._params["stock_name"] = stock_name
        return self.steps("../datas/step/search.yml", "is_choose")
