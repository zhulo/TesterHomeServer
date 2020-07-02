# -*- encoding: utf-8 -*-
"""
@File    : locusts.py
@Time    : 2020/7/1 20:52
@Author  : tester
@Software: PyCharm
"""

import random

from locust import TaskSet, task, HttpUser

from Icncde.OpenApi import consts as c
from Icncde.OpenApi.client import header_param_without_base_info
from common.utils.logger import Logger

log = Logger(__name__).log()

instrument_id = c.CurrencyInfo.currency_code
best_ask = c.CurrencyInfo.best_ask
best_bid = c.CurrencyInfo.best_bid


class OpenApiTest(TaskSet):
    def taker_order_with_sell(self, account):
        sell_value = round(random.uniform(c.CurrencyInfo.best_ask, c.CurrencyInfo.best_bid), 2)
        end_point = '/openapi/spot/v1/orders'
        params = {'instrument_Id': instrument_id, 'side': 'S', 'type': 'LIMIT', 'size': '0.01',
                  'price': str(sell_value)}
        header, param = header_param_without_base_info("POST", end_point, params, use_server_time=False, **account)
        resp = self.client.post(end_point, headers=header, data=param)
        log.info("用户: {}, 下单卖出价格： {}, 接口返回： {}".format(account['email'], sell_value, resp.json()))
        sell_value = sell_value + random.randint(20, 30)
        params = {'instrument_Id': instrument_id, 'side': 'B', 'type': 'LIMIT', 'size': '0.01',
                  'price': str(sell_value + 1)}
        header, param = header_param_without_base_info("POST", end_point, params, use_server_time=False, **account)
        resp = self.client.post(end_point, headers=header, data=param)
        log.info("用户: {}, 下单买入价格： {}, 接口返回： {}".format(account['email'], sell_value, resp.json()))

    @task(1)
    def taker_order_with_sell_user_01(self):
        account = c.OpenApiAccount.open_api_user_001
        self.taker_order_with_sell(account)

    @task(1)
    def taker_order_with_sell_user_02(self):
        account = c.OpenApiAccount.open_api_user_002
        self.taker_order_with_sell(account)

    @task(1)
    def taker_order_with_sell_user_03(self):
        account = c.OpenApiAccount.open_api_user_003
        self.taker_order_with_sell(account)

    @task(1)
    def taker_order_with_sell_user_04(self):
        account = c.OpenApiAccount.open_api_user_004
        self.taker_order_with_sell(account)

    @task(1)
    def taker_order_with_sell_user_05(self):
        account = c.OpenApiAccount.open_api_user_005
        self.taker_order_with_sell(account)


class WebsiteUser(HttpUser):
    tasks = [OpenApiTest]
    min_wait = 100
    max_wait = 1000
    host = c.API_URL
