'''
 -*- coding: utf-8 -*-
 @Time    : 2020/8/9 9:42
 @Author  : Summer
 @Email   : 2361157192@qq.com
 @File    : test_requests.py
 
 '''
import json

import requests
from jsonpath import jsonpath
from hamcrest import *
from jsonschema import validate
from requests.auth import HTTPBasicAuth


class TestRequests:

    def test_get(self):
        r = requests.get('https://api.github.com/events')
        print(r.text)
        print(r.status_code)
        assert r.status_code == 200

    def test_query(self):
        payload = {
            "level": 1,
            "name": "summer"
        }
        r = requests.get('https://httpbin.testing-studio.com/get', params=payload)
        print(r.text)

        assert r.status_code == 200

    def test_form(self):
        payload = {
            "key1": "value1",
            "key2": "value2"
        }
        r = requests.post("https://httpbin.testing-studio.com/post", data=payload)
        print(r.text)
        assert r.status_code == 200

    def test_header(self):
        r = requests.get('https://httpbin.testing-studio.com/get', headers={"h": "header"})
        print(r.text)
        print(r.status_code)
        print(r.json())

        assert r.status_code == 200

    def test_post_json(self):
        payload = {
            "key1": "value1",
            "key2": "value2"
        }
        r = requests.post("https://httpbin.testing-studio.com/post", json=payload)
        print(r.text)
        assert r.status_code == 200
        assert r.json()['json']['key1'] == 'value1'

    def test_assert_json(self):
        r = requests.get("https://ceshiren.com/categories.json")
        print(r.text)
        assert r.status_code == 200
        assert r.json()['category_list']['categories'][0]['name'] == '社区治理'

    def test_json_path(self):
        url = "https://ceshiren.com/categories.json"
        r = requests.get(url)
        assert r.json()['category_list']['categories'][0]['name'] == '社区治理'
        print(jsonpath(r.json(), '$..name'))
        assert jsonpath(r.json(), '$..name')[0] == '社区治理'

    def test_hamcrest(self):
        url = "https://ceshiren.com/categories.json"
        r = requests.get(url)
        assert_that(r.json()['category_list']['categories'][0]['name'], equal_to('社区治理'))

    def test_schema(self):
        url = "https://testerhome.com/api/v3/topics.json"
        data = requests.get(url, params={'limit': '2'}).json()
        schema = json.load(open("topic_schema.json"))
        validate(data, schema=schema)

    def test_cookie(self):
        url = "https://httpbin.testing-studio.com/cookies"
        headers = {"Cookie": 'working=1', 'User-Agent': 'python-requests/2.23.0'}
        r = requests.get(url, headers=headers)
        print(r.request.headers)

    def test_oauth(self):
        r = requests.get(url="https://httpbin.testing-studio.com/basic-auth/banana/123",
                         auth=HTTPBasicAuth("banana", "123"))

        print(r.text)
