# -*- encoding: utf-8 -*-
"""
@File    : wsc_test_trade_coin.py
@Time    : 2020/7/13 18:04
@Author  : tester
@Software: PyCharm
"""

from locust import TaskSet, HttpUser
from locust import events

from Icncde.trade import consts as c
from Icncde.trade.trade_server import get_access_token_with_headers_list

headers = []


class WscTestTradeCoin(TaskSet):
    @events.test_start.add_listener
    def on_test_start(**kwargs):
        users_headers = get_access_token_with_headers_list(c.HOST, c.EmailLoginAPI, c.Headers, 't1@163.com',
                                                           c.Password)
        headers.append(users_headers)

    def trade_coin(self):
        pass


class WebsiteUser(HttpUser):
    tasks = [WscTestTradeCoin]

    min_wait = 100
    max_wait = 1000
    host = "http://test.mobile.icctoro.com:7007"
