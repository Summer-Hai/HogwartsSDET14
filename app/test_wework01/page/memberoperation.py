# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/29 12:52
# @Author  : Summer
# @Email    : 2361157192@qq.com
# @File    : memberoperation.py
# @Software: PyCharm

"""
用户操作页面
"""
import allure
from appium.webdriver.common.mobileby import MobileBy

from app.test_wework01.page.basepage import BasePage
from app.test_wework01.page.userinfo import UserInfo


class MemberOperation(BasePage):
    moreMemberOperation_element = (MobileBy.ID, "com.tencent.wework:id/h9p")

    def moreMemberOperation(self):
        """
        点击更多设置功能，进入用户信息页面
        :return:
        """
        with allure.step("点击更多设置，进入用户编辑页面"):
            self.find_and_click(self.moreMemberOperation_element)
        return UserInfo(self.driver)
