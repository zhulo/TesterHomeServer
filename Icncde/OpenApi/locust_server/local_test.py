# -*- encoding: utf-8 -*-
"""
@File    : local_test.py
@Time    : 2020/7/2 16:46
@Author  : tester
@Software: PyCharm
"""

import random

from locust import TaskSet, task, HttpUser

from Icncde.OpenApi import consts as c
from Icncde.OpenApi.client import header_param_without_base_info

# currency_code = c.CurrencyInfo.currency_code
currency_code_list = c.CurrencyInfo.currency_code_list
best_ask = c.CurrencyInfo.best_ask
best_bid = c.CurrencyInfo.best_bid
sell_with_buy = c.CurrencyInfo.sell_with_buy

account_list = c.OpenApiAccount.account


class CurrencyTrade(TaskSet):
    def order_task(self, account, currency_code, sell=True, amount=None):
        open_api_order = '/openapi/spot/v1/orders'
        if sell:
            if amount is None:
                amount = str(random.uniform(1, 10))
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            price = round(_price, 2)
            params = {'instrument_Id': currency_code, 'side': 'S', 'type': 'LIMIT', 'size': amount, 'price': str(price)}
        else:
            if amount is None:
                amount = str(random.uniform(1, 10))
            _price = random.uniform(best_ask + sell_with_buy, best_bid + sell_with_buy)  # 买入的价格
            price = round(_price, 2)
            params = {'instrument_Id': currency_code, 'side': 'B', 'type': 'LIMIT', 'size': amount, 'price': str(price)}
        header, param = header_param_without_base_info("POST", open_api_order, params, use_server_time=False, **account)
        resp = self.client.post(open_api_order, headers=header, data=param)
        # assert str(resp.status_code) == '200'
        if sell:
            print("用户: {}, 币对: {}, 卖出数量 {}, 卖出价格： {}, 接口返回： {}".format(account['email'], currency_code, amount, price,
                                                                       resp.json()))
        else:
            print("用户: {},币对: {}, 卖出数量 {}, 买入价格： {}, 接口返回： {}".format(account['email'], currency_code, amount, price,
                                                                      resp.json()))

    @task(1)
    def order_sell_01(self):
        self.order_task(account_list[0], "DSSJ_USDT_ICNCDE_ENCRY")

    @task(1)
    def order_buy_01(self):
        self.order_task(account_list[0], "DSSJ_USDT_ICNCDE_ENCRY", False)


class WebsiteUser(HttpUser):
    tasks = [CurrencyTrade]
    min_wait = 100
    max_wait = 1000
    host = 'http://test.mobile.icctoro.com:7007'

# no web 执行 locust -f Icncde\OpenApi\locust_server\open_api_task.py --headless -u 10 -r 10 -t 10s
