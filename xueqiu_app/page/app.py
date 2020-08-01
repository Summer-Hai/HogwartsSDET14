'''
 -*- coding: utf-8 -*-
 @Time    : 2020/7/30 20:20
 @Author  : Summer
 @Email   : 2361157192@qq.com
 @File    : app.py
 
 '''

import allure
from appium import webdriver

from app.test_wework01.page.basepage import BasePage
from app.test_wework01.page.mainpage import MainPage
from xueqiu_app.page.main import Main


class App(BasePage):
    _apppackage = "com.xueqiu.android"
    _appActivity = ".view.WelcomeActivityAlias"

    def start(self):
        """
        启动app
        """
        with allure.step("调用start方法进行初始化"):
            if self.driver == None:
                # 第一次调用start（）方法的时候driver 为None
                caps = {}
                caps["platformName"] = "Android"
                caps["deviceName"] = "emulator-5554"
                caps["appPackage"] = self._apppackage
                caps["appActivity"] = self._appActivity
                caps["noReset"] = "true"
                self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
                # self.driver.implicitly_wait(15)

            else:
                self.driver.launch_app()
            self.driver.implicitly_wait(20)
        return self

    def restart(self):
        """
        重启App
        """
        with allure.step("调用restart方法进行重启app"):
            self.driver.close()
            self.driver.launch_app()
        return self

    def stop(self):
        """
        停止App
        """
        with allure.step("调用stop方法进行关闭app"):
            self.driver.quit()

    def goto_main(self):
        """
        进入首页
        """
        with allure.step("进入首页"):
            return Main(self.driver)
