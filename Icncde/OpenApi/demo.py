# -*- encoding: utf-8 -*-
"""
@File    : locust_file.py
@Time    : 2020/7/1 20:52
@Author  : tester
@Software: PyCharm
"""

from locust import TaskSet, task, HttpUser


class OpenApiTest(TaskSet):

    # def taker_order_with_sell_01(self, test):
    #     print(test)

    @task(1)
    def taker_order_with_sell_02(self):
        print('---------' * 20)

    @task(10)
    def taker_order_with_sell_03(self):
        print('+++++++++++++++++++++++++++')


class WebsiteUser(HttpUser):
    tasks = [OpenApiTest]
    min_wait = 100
    max_wait = 10000
    host = ''
