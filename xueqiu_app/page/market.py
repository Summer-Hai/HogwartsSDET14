'''
 -*- coding: utf-8 -*-
 @Time    : 2020/7/30 20:20
 @Author  : Summer
 @Email   : 2361157192@qq.com
 @File    : market.py
 
 '''
import allure
import yaml
from appium.webdriver.common.mobileby import MobileBy

from xueqiu_app.page.base_page import BasePage
from xueqiu_app.page.search import Search


class Market(BasePage):

    def goto_serach(self):
        # self.find(MobileBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/action_search']").click()
        # ------- 下面是第二次修改  -------
        # with open("../datas/step/market.yml", encoding="UTF-8") as f:
        #     steps = yaml.safe_load(f)
        # for step in steps:
        #     if "action" in step.keys():
        #         action = step["action"]
        #         if action == "click":
        #             self.find(step["by"],step["locator"]).click()
        with allure.step("点击搜索"):
            self.steps("../datas/step/market.yml", "goto_serach")
        return Search(self.driver)
