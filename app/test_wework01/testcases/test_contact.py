'''
 -*- coding: utf-8 -*-
 @Time    : 2020/7/27 22:37
 @Author  : Summer
 @Email   : 2361157192@qq.com
 @File    : test_contact.py
 
 '''
import allure
import pytest
import yaml

from app.test_wework01.page.app import App

with open('../datas/addcontact.yml', encoding="UTF-8") as f:
    addcontactdatas = yaml.safe_load(f)
    print(addcontactdatas)

with open('../datas/delcontact.yml', encoding="UTF-8") as f:
    delcontactdatas = yaml.safe_load(f)
    print(delcontactdatas)


class TestContact:

    def setup_class(self):
        self.app = App()
        self.main = self.app.start().goto_main()

    @allure.story("添加成员")
    @pytest.mark.parametrize('name,gender,phonenum', addcontactdatas)
    def test_addcontact(self, name, gender, phonenum):
        # name = "Summer04"
        # gender = "女"
        # phonenum = "13000008884"
        with allure.step("调用添加方法"):
            mypage = self.main.goto_contactlist(). \
                addcontact().add_menual(). \
                set_name(name).set_gender(gender).set_phonenum(phonenum).click_save()

        text = mypage.get_toast()

        assert '成功' in text

        self.app.back()

    @allure.story("删除成员")
    @pytest.mark.parametrize('name', delcontactdatas)
    def test_delcontact(self, name):
        with allure.step("调用添加方法"):
            num = self.main.goto_contactlist(). \
                search_contact().search_name(name). \
                moreMemberOperation().update_userinfo(). \
                delmenber().checkout_search_name(name)
        assert num == 1

        self.main.back()
