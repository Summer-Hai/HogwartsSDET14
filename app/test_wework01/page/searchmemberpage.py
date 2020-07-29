#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/29 12:32
# @Author  : Summer
# @Email    : 2361157192@qq.com
# @File    : searchmemberpage.py
# @Software: PyCharm
"""
搜索页面操作
"""
from time import sleep

import allure
from appium.webdriver.common.mobileby import MobileBy

from app.test_wework01.page.basepage import BasePage
from app.test_wework01.page.memberoperation import MemberOperation


class SearchMemberPage(BasePage):
    search_element = (MobileBy.ID, "com.tencent.wework:id/fxc")

    # num = 0

    def search_name(self, name):
        search_name_element = (MobileBy.XPATH, f"//*[@text='{name}']")
        """
        点击搜索框设置搜索名称
        点击搜索
        选择对应用户进行操作点击进入用户操作界面
        这里我把搜索用户的数量存到num.txt的文件
        
        :param name:
        :return:
        """
        with allure.step(f"点击搜索框输入数据{name}"):
            self.find_and_sendkeys(self.search_element, name)

        sleep(3)
        with allure.step(f"查找所有关于{name}的用户"):
            elelist = self.finds(search_name_element)

        with allure.step(f"判断{name}相关的用户数量是否大于2"):
            if len(elelist) < 2:
                print("没有这个联系人")
                return
        # self.num = len(elelist)
        num = len(elelist)
        # 把num存到文件中
        with open("../datas/num.txt", 'w') as f:
            f.write(str(num))

        with allure.step("点击顶置的用户（要删除的用户），进入用户详情页"):
            elelist[1].click()

        return MemberOperation(self.driver)

    def checkout_search_name(self, name):
        checkout_search_name_element = (MobileBy.XPATH, f"//*[@text='{name}']")

        """
        对比搜索前和搜索后的人数判断否删除成功：
        :return: 搜索前和搜索后想减的人数
        """

        with open('../datas/num.txt', encoding="UTF-8") as f:
            num = int(f.read())
            print(num)

        sleep(3)
        with allure.step("删除检验"):
            self.elelist_after = self.finds(checkout_search_name_element)

        # return self.num - len(self.elelist_after)  不知道为什么self.num=0???  所以没有办法只能把num的值存在num.txt（覆盖式存储）
        return num - len(self.elelist_after)
