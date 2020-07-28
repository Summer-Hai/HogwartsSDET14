'''
 -*- coding: utf-8 -*-
 @Time    : 2020/7/26 16:12
 @Author  : Summer
 @Email   : 2361157192@qq.com
 @File    : app.py

 存放 app 应用常用的一些方法：比如启动app、关闭app，停止app ，进入首页

 '''
from appium import webdriver

from app.test_wework01.page.basepage import BasePage
from app.test_wework01.page.mainpage import MainPage


class App(BasePage):
    def start(self):
        """
        启动app
        """
        if self.driver == None:
            # 第一次调用start（）方法的时候driver 为None
            caps = {}
            caps["platformName"] = "Android"
            caps["deviceName"] = "emulator-5554"
            caps["appPackage"] = "com.tencent.wework"
            caps["appActivity"] = ".launch.WwMainActivity"
            caps["noReset"] = "true"
            # caps["dontStopAppOnReset"] = "true"
            caps["skipDeviceInitialization"] = "true"
            caps["unicodeKeyBoard"] = "true"
            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
            self.driver.implicitly_wait(15)

        else:
            # launch_app() 这个方法不需要传入任何参数， 会自动启动起来DesireCapa里面定义的activity
            # start_activity(packagename, activityname) 可以启动其它的应用的页面
            self.driver.launch_app()
            self.driver.implicitly_wait(15)

        return self

    def restart(self):
        """
        重启App
        """
        self.driver.close()
        self.driver.launch_app()
        return self

    def stop(self):
        """
        停止App
        """
        self.driver.quit()

    def goto_main(self):
        """
        进入首页
        """
        return MainPage(self.driver)
