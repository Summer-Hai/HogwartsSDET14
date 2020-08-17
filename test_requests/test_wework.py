'''
 -*- coding: utf-8 -*-
 @Time    : 2020/8/16 10:47
 @Author  : Summer
 @Email   : 2361157192@qq.com
 @File    : test_wework.py
 
 '''
import json

import pytest
import requests


def test_create_datas():
    datas = [("kenan%02d" % x,
              "柯南",
              "130%08d" % x) for x in range(1, 12)]

    print(datas)
    return datas


class TestWework():
    @pytest.fixture(scope="session")
    def token(self):
        request_params = {
            "corpid": "ww4b219242adca5658",
            "corpsecret": "WSMJARc1RM91scB9wl9OLJKsrCJglry_S76wLJ05kIg"
        }
        r = requests.get(" https://qyapi.weixin.qq.com/cgi-bin/gettoken", params=request_params)
        print(r.status_code)
        print(r.json())

        return r.json()['access_token']

    def test_create(self, token, userid, mobile, name):
        # access_token = self.get_token()
        request_body = {
            "userid": userid,
            "name": name,
            "mobile": mobile,
            "department": [1]
        }
        json.dumps(request_body)
        r = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={token}", json=request_body)
        print(r.status_code)
        print(r.json())

        return r.json()

    def test_get_user(self, token, userid):
        # access_token = self.get_token()

        r = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={token}&userid={userid}")

        print(r.json())
        return r.json()

    def test_update_user(self, token, userid, mobile, name):
        """
        请求地址：https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token=ACCESS_TOKEN
        """
        # access_token = self.get_token()
        request_boay = {
            "userid": userid,
            "name": name,
            "mobile": mobile,
        }
        r = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={token}", json=request_boay)

        return r.json()

    def test_delete_user(self, token, userid):
        """
        请求地址：https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token=ACCESS_TOKEN&userid=USERID
        """

        r = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={token}&userid={userid}")

        return r.json()

    @pytest.mark.parametrize("userid, name, mobile", test_create_datas())
    def test_wework(self, token, userid, name, mobile):
        """
        整体测试：

        """

        assert 'created' == self.test_create(token, userid, mobile, name)['errmsg']
        assert name == self.test_get_user(token, userid)['name']
        assert "updated" == self.test_update_user(token, userid, mobile, "肯恩555")["errmsg"]
        assert "肯恩555" == self.test_get_user(token, userid)['name']
        assert "deleted" == self.test_delete_user(token, userid)['errmsg']
        assert 60111 == self.test_get_user(token, userid)['errcode']
