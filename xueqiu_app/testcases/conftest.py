'''
 -*- coding: utf-8 -*-
 @Time    : 2020/8/4 22:13
 @Author  : Summer
 @Email   : 2361157192@qq.com
 @File    : conftest.py
 
 '''
import os
import signal
import subprocess

import pytest


@pytest.fixture(scope="class", autouse=True)
def record():
    cmd = "scrcpy --record tmp.mp4"
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    yield
    os.kill(p.pid, signal.CTRL_C_EVENT)
