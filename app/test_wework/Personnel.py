'''
 -*- coding: utf-8 -*-
 @Time    : 2020/7/25 23:22
 @Author  : Summer
 @Email   : 2361157192@qq.com
 @File    : Personnel.py
 
 '''
from time import sleep
import allure
from appium.webdriver.webdriver import WebDriver

from app.test_wework.base import Base


class Personnel(Base):

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def add_user(self, username):
        # 点击添加成员
        with allure.step("点击添加成员"):
            self.driver.find_element_by_xpath("//*[@class='android.widget.TextView' and  @text='添加成员']").click()
        # 点击手动输入添加
        with allure.step("点击手动输入添加"):
            self.driver.find_element_by_xpath("//*[@class='android.widget.TextView' and @text='手动输入添加']").click()
        # 点击名称输入框进行姓名设置summer
        with allure.step("点击姓名输入框进行输入添加"):
            self.driver.find_element_by_xpath("//*[@class='android.widget.EditText' and @text='必填']").send_keys(
                f'{username}')
        # 点击手机号码输入手机号码：13000008888
        with allure.step("点击手机号码输入框点击输入13000008888"):
            self.driver.find_element_by_id("com.tencent.wework:id/f1e").send_keys("13000008888")
        # 点击设置部门进入部门设置界面
        with allure.step("点击设置部门"):
            self.driver.find_element_by_xpath("//*[@resource-id='com.tencent.wework:id/axm' and @text='设置部门']").click()
        # 点击部门确定
        with allure.step("点击点击确定功能"):
            self.driver.find_element_by_id("com.tencent.wework:id/g09").click()
        # 点击弹窗进行点击确定功能
        with allure.step("点击弹窗的确定功能"):
            self.driver.find_element_by_id("com.tencent.wework:id/h9w").click()
        # 预防模拟器卡顿
        sleep(5)

        # 点击返回用户列表
        with allure.step("点击返回用户列表"):
            self.driver.find_element_by_id("com.tencent.wework:id/h9e").click()

        element = self.driver.find_element_by_xpath("//*[@text='summer']")

        if element != None:
            print("添加用户成功")
            return True
        else:
            print("添加用户失败")
            return False

    def del_user(self, username):

        # 删除summer用户定位   android.widget.ListView
        with allure.step(f"点击{username}用户"):
            self.driver.find_element_by_xpath(f"//*[@text='{username}']").click()

        # 点击更多功能
        with allure.step("点击更多功能"):
            self.driver.find_element_by_id("com.tencent.wework:id/h9p").click()

        sleep(3)
        # 点击用户编辑功能
        with allure.step("点击用户编辑功能"):
            self.driver.find_element_by_id("com.tencent.wework:id/b2c").click()

        # 点击删除用户功能
        with allure.step("点击删除用户功能"):
            self.driver.find_element_by_xpath("//*[@text='删除成员']").click()

        # 点击弹窗确定功能
        with allure.step("点击弹窗确定功能"):
            self.driver.find_element_by_id("com.tencent.wework:id/bci").click()

        try:
            self.driver.find_element_by_xpath("//*[@text='summer']")

        except:
            print("删除用户成功")
            return True

        else:
            print("删除用户失败")
            return False
