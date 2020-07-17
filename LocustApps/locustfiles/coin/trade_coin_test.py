# -*- encoding: utf-8 -*-
"""
@File    : trade_coin_test.py
@Time    : 2020/7/16 18:50
@Author  : tester
@Software: PyCharm
"""

from locust import TaskSet, task
from locust import events

code_list = ['code1', 'code2', 'code3']


class HttpTest(TaskSet):

    @events.test_start.add_listener
    def on_test_start(**kwargs):
        pass
    '''如何根据code_list的长度生成多个task?'''
    @task
    def task_code_01(self):
        print(code_list[0])

    @task
    def task_code_01(self):
        print(code_list[1])

    @task
    def task_code_01(self):
        print(code_list[2])
