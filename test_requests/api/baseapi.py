'''
 -*- coding: utf-8 -*-
 @Time    : 2020/8/16 16:23
 @Author  : Summer
 @Email   : 2361157192@qq.com
 @File    : baseapi.py
 
 '''
import json
import logging

import requests


class BaseApi():
    logging.basicConfig(level=logging.INFO)

    params = {}

    def send(self, datas):
        logging.info(f"run--send  接口访问,{datas}")

        raw_data = json.dumps(datas)
        for key, value in self.params.items():
            raw_data = raw_data.replace("${" + key + "}", value)
        datas = json.loads(raw_data)
        # print(datas)
        return requests.request(**datas).json()
