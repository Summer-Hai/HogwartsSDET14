'''
 -*- coding: utf-8 -*-
 @Time    : 2020/8/16 16:15
 @Author  : Summer
 @Email   : 2361157192@qq.com
 @File    : util.py
 
 '''
import requests


class Util():

    def get_token(self):
        request_params = {
            "corpid": "ww4b219242adca5658",
            "corpsecret": "WSMJARc1RM91scB9wl9OLJKsrCJglry_S76wLJ05kIg"
        }
        r = requests.get(" https://qyapi.weixin.qq.com/cgi-bin/gettoken", params=request_params)
        return r.json()['access_token']
