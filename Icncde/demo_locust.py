# -*- encoding: utf-8 -*-
"""
@File    : demo_locust.py
@Time    : 2020/7/15 18:02
@Author  : tester
@Software: PyCharm
"""

import random

from locust import TaskSet, HttpUser, task


class DemoTest(TaskSet):
    def fun_01(self, name):
        amount = str(random.uniform(1, 10))
        print(str(name) + '-----' + str(amount))

    @task
    def demo_001(self):
        self.fun_01('demo_001')

    @task
    def demo_002(self):
        self.fun_01('demo_002')

    @task
    def demo_003(self):
        self.fun_01('demo_003')

    @task
    def demo_004(self):
        self.fun_01('demo_004')


class WebsiteUser(HttpUser):
    tasks = [DemoTest]

    min_wait = 1000
    max_wait = 10000
    host = "http://test.mobile.icctoro.com:7007"
