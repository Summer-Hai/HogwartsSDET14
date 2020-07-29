#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/29 13:01
# @Author  : Summer
# @Email    : 2361157192@qq.com
# @File    : delmember.py
# @Software: PyCharm
"""
删除用户
"""
# from app.test_wework01.page.searchmemberpage import SearchMemberPage
import allure
from appium.webdriver.common.mobileby import MobileBy

from app.test_wework01.page.basepage import BasePage


class DelMember(BasePage):
    del_element = (MobileBy.ID, "com.tencent.wework:id/e3f")
    check_del_element = (MobileBy.ID, "com.tencent.wework:id/bci")

    def delmenber(self):
        """
        点删除功能删除用户
        确定删除用户
        :return:
        """
        with allure.step("点击删除成员功能，删除用户"):
            self.find_and_click(self.del_element)
            # 7.确认删除
        with allure.step("点击确定功能，确定删除用户"):
            self.find_and_click(self.check_del_element)
        from app.test_wework01.page.searchmemberpage import SearchMemberPage
        return SearchMemberPage(self.driver)
