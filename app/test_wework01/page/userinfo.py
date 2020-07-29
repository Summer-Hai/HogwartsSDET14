#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/29 12:56
# @Author  : Summer
# @Email    : 2361157192@qq.com
# @File    : userinfo.py
# @Software: PyCharm

"""
用户信息页面
"""
import allure
from appium.webdriver.common.mobileby import MobileBy

from app.test_wework01.page.basepage import BasePage
from app.test_wework01.page.delmember import DelMember


class UserInfo(BasePage):
    update_userinfo_element = (MobileBy.ID, "com.tencent.wework:id/b2c")

    def update_userinfo(self):
        """
        点击拜编辑成员，进入用户信息详情页
        :return:
        """
        with allure.step("点击编辑，进入用户信息编辑页面"):
            self.find_and_click(self.update_userinfo_element)
        return DelMember(self.driver)
