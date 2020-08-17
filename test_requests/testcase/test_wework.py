'''
 -*- coding: utf-8 -*-
 @Time    : 2020/8/16 16:12
 @Author  : Summer
 @Email   : 2361157192@qq.com
 @File    : test_wework.py
 
 '''
import allure

from test_requests.api.wework import Wework


@allure.feature("企业微信接口测试")
class TestWework():
    """
    用户测试case
    """

    @allure.story("用户操作接口测试")
    @allure.title("新建用户")
    @allure.step("新建用户")
    def test_created_user(self):
        userid = "kenan02"
        # print(Wework().test_create_user(userid, "13000005555", "柯南"))
        try:
            assert 'created' == Wework().test_create_user(userid, "13000005555", "柯南")['errmsg']
            with allure.step("成功新建用户"):
                print("成功新建userid为kenan02的用户")
        except Exception as e:
            with allure.step("新建用户失败"):
                print("新建userid为kenan02的用户失败")

            raise e

    @allure.story("用户操作")
    @allure.title("获取用户")
    @allure.step("获取用户")
    def test_get_user(self):
        userid = "kenan02"
        # print(Wework().test_get_user(userid))
        try:
            assert "柯南" == Wework().test_get_user(userid)['name']
            with allure.step("成功获取用户"):
                print("成功获取userid为kenan02的用户")
        except Exception as e:
            with allure.step("获取用户失败"):
                print("获取userid为kenan02的用户失败")
            raise e

    @allure.story("用户操作")
    @allure.title("更新用户")
    @allure.step("更新用户")
    def test_update_user(self):
        # print(Wework().test_update_user("kenan02", "13000005555", "柯南1"))
        try:
            assert 'updated' == Wework().test_update_user("kenan02", "13000005555", "柯南1")['errmsg']
            with allure.step("成功更新用户"):
                print("成功更新userid为kenan02的用户")
        except Exception as e:
            with allure.step("更新用户失败"):
                print("更新userid为kenan02的用户失败")

            raise e

    @allure.story("用户操作")
    @allure.title("删除用户")
    @allure.step("删除用户")
    def test_deleted_user(self):
        # print(Wework().test_deleted_user("kenan02"))
        try:
            assert 'deleted' == Wework().test_deleted_user("kenan02")['errmsg']
            with allure.step("成功删除用户"):
                print("成功删除userid为kenan02的用户")
        except Exception as e:
            with allure.step("删除用户失败"):
                print("删除userid为kenan02的用户失败")

            raise e

    """
    标签测试case
    """

    @allure.story("标签操作接口测试")
    @allure.title("新建标签")
    @allure.step("新建标签")
    def test_created_tag(self):
        # print(Wework().create_tag("UI", "01"))
        try:
            assert "created" == Wework().create_tag("java", "102")['errmsg']
            with allure.step("成功新建标签"):
                print("成功新建tagid为102的标签")
        except Exception as e:
            with allure.step("新建标签失败"):
                print("新建tagid为102的标签失败")

            raise e

    # def test_add_tag_member(self):
    #     print(Wework().add_tag_member("102"))

    @allure.story("标签操作接口测试")
    @allure.title("获取标签成员")
    @allure.step("获取标签成员")
    def test_get_tag_member(self):
        # print(Wework().get_tag_member("102"))
        try:
            assert "summer01" == Wework().get_tag_member("101")["userlist"][0]['userid']
            with allure.step("成功获取标签用户"):
                print("成功获取tagid为101的标签用户")
        except Exception as e:
            with allure.step("获取标签用户失败"):
                print("获取tagid为101的标签用户失败")
            raise e

    @allure.story("标签操作接口测试")
    @allure.title("更新标签")
    @allure.step("更新标签")
    def test_updated_tag(self):
        # print(Wework().update_tag("Java开发", "102"))
        try:
            assert 'updated' == Wework().update_tag("Java开发", "102")['errmsg']
            with allure.step("标签更新成功"):
                print("成功更新tagid为102的标签")
        except Exception as e:
            with allure.step("标签更新失败"):
                print("更新tagid为102的标签失败")
            raise e

    @allure.story("标签操作接口测试")
    @allure.title("删除标签")
    @allure.step("删除标签")
    def test_deleted_tag(self):
        # print(Wework().deleted_tag("102"))
        try:
            assert "deleted" == Wework().deleted_tag("102")['errmsg']
            with allure.step("标签删除成功"):
                print("成功删除tagid为102的标签")
        except Exception as e:
            with allure.step("标签删除失败"):
                print("删除tagid为102的标签失败")
            raise e
