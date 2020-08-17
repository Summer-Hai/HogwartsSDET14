'''
 -*- coding: utf-8 -*-
 @Time    : 2020/8/16 16:10
 @Author  : Summer
 @Email   : 2361157192@qq.com
 @File    : wework.py
 
 '''
import logging

import yaml

from test_requests.api.baseapi import BaseApi
from test_requests.api.util import Util


class Wework(BaseApi):
    logging.basicConfig(level=logging.INFO)

    def __init__(self):
        self.token = Util().get_token()
        self.params["token"] = self.token

    """
     用户的增删改查
    """

    def test_create_user(self, userid, mobile, name):
        logging.info(f"run--test_create_user 参数：userid = {userid}, mobile = {mobile}, name = {name}")

        department = "1"
        # data = {
        #     "method": "post",
        #     "url": f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.token}",
        #     "json":  {
        #             "userid": userid,
        #             "name": name,
        #             "mobile": mobile,
        #             "department": department
        #         }
        # }
        self.params["userid"] = userid
        self.params["name"] = name
        self.params["mobile"] = mobile
        self.params["department"] = department

        with open("../datas/wework.yml", encoding="utf-8") as f:
            data = yaml.safe_load(f)["create_user"]

        return self.send(data)

    def test_get_user(self, userid):
        # data = {
        #     "method": "get",
        #     "url": f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={self.token}&userid={userid}"
        # }
        logging.info(f"run--test_get_user 参数：userid = {userid}")
        self.params["userid"] = userid
        with open("../datas/wework.yml", encoding="utf-8") as f:
            data = yaml.safe_load(f)["get_user"]
        return self.send(data)

    def test_update_user(self, userid, mobile, name):
        """
        请求地址：https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token=ACCESS_TOKEN
        """
        # access_token = self.get_token()
        # request_boay = {
        #     "userid": userid,
        #     "name": name,
        #     "mobile": mobile,
        # }
        # r = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={self.token}", json=request_boay)
        #
        # data = {
        #     "method": "post",
        #     "url": f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={self.token}",
        #     "json": {
        #         "userid": userid,
        #         "name": name,
        #         "mobile": mobile,
        #     }
        # }
        logging.info(f"run--test_update_user 参数：userid = {userid}, mobile = {mobile}, name = {name}")
        self.params["userid"] = userid
        self.params["mobile"] = mobile
        self.params["name"] = name
        with open("../datas/wework.yml", encoding="utf-8") as f:
            data = yaml.safe_load(f)["update_user"]
        return self.send(data)

    def test_deleted_user(self, userid):
        """
        请求地址：https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token=ACCESS_TOKEN&userid=USERID
        """
        # data = {
        #     "method": "post",
        #     "url": f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={self.token}&userid={userid}"
        # }
        logging.info(f"run--test_deleted_user 参数：userid = {userid}")
        self.params["userid"] = userid
        with open("../datas/wework.yml", encoding="utf-8") as f:
            data = yaml.safe_load(f)["deleted_user"]
        return self.send(data)

    """
     标签的增删改查
    """

    def create_tag(self, tagname, tagid):
        logging.info(f"run--create_tag 创建标签 参数：tagname = {tagname}, tagid = {tagid}")
        self.params["tagname"] = tagname
        self.params["tagid"] = tagid
        with open("../datas/wework.yml", encoding="utf-8") as f:
            data = yaml.safe_load(f)["create_tag"]
        return self.send(data)

    def get_tag_member(self, tagid):
        logging.info(f"run--get_tag_member 获取标签成员 参数：tagid = {tagid}")
        self.params["tagid"] = tagid
        with open("../datas/wework.yml", encoding="utf-8") as f:
            data = yaml.safe_load(f)["get_tag"]
        return self.send(data)

    def update_tag(self, tagname, tagid):
        logging.info(f"run--update_tag 更新标签 参数：tagname = {tagname}, tagid = {tagid}")
        self.params["tagname"] = tagname
        self.params["tagid"] = tagid
        with open("../datas/wework.yml", encoding="utf-8") as f:
            data = yaml.safe_load(f)["update_tag"]
        return self.send(data)

    def deleted_tag(self, tagid):
        logging.info(f"run--deleted_tag 删除标签 参数：tagid = {tagid}")
        self.params["tagid"] = tagid
        with open("../datas/wework.yml", encoding="utf-8") as f:
            data = yaml.safe_load(f)["deleted_tag"]
        return self.send(data)

    # def add_tag_member(self, tagid):
    #     department = None
    #     self.params['tagid'] = tagid
    #     # self.params['userid1'] = userid1
    #     # self.params['userid2'] = userid2
    #     self.params['department'] = department
    #     with open("../datas/wework.yml", encoding="utf-8") as f:
    #         data = yaml.safe_load(f)["add_tag_member"]
    #     return self.send(data)
