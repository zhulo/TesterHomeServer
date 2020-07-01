# -*- encoding: utf-8 -*-
"""
@File    : locusts.py
@Time    : 2020/7/1 20:52
@Author  : tester
@Software: PyCharm
"""

from locust import TaskSet, task, HttpUser


class OpenApiTest(TaskSet):

    def taker_order_with_sell_01(self, test):
        print(test)

    @task(1)
    def taker_order_with_sell_02(self):
        self.taker_order_with_sell_01(11111111111111111111)
        print('------------------------')

    @task(1)
    def taker_order_with_sell_03(self):
        self.taker_order_with_sell_01(22222222222222222)
        print('+++++++++++++++++++++++++++')


class WebsiteUser(HttpUser):
    tasks = [OpenApiTest]
    min_wait = 100
    max_wait = 10000
    host = ''
