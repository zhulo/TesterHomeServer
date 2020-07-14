# -*- encoding: utf-8 -*-
"""
@File    : trade_locust.py
@Time    : 2020/7/9 14:54
@Author  : tester
@Software: PyCharm
"""

import random
import threading

from locust import TaskSet, HttpUser, task
from locust import events

from Icncde.trade import consts as c
from Icncde.trade.trade_server import TradeCoinSetUpData, get_access_token_with_headers_list

setup_trade_coin_data = TradeCoinSetUpData(c.HOST)
code_list = c.TradeCoinList
best_ask = 0
best_bid = 1000
headers_list = get_access_token_with_headers_list(c.HOST, c.EmailLoginAPI, c.Headers, c.UsernameList,
                                                  c.Password)


class HttpTradeCoin(TaskSet):

    @events.test_start.add_listener
    def on_test_start(**kwargs):
        tasks = []

        if headers_list is False:
            exit()

        # :param headers:
        # :param initial_price: 初始买入卖出价格
        # :param trade_coin_num: 单个盘口的总委托数
        # :param user_num: 用户总数
        # :param trade_highly: 单个币对的盘口深度
        # :param amount: 单个委托单的委托数量
        for i in range(len(headers_list)):
            # print(headers_list[i])
            t = threading.Thread(target=TradeCoinSetUpData(c.HOST).one_headers_trade_coin,
                                 args=(headers_list[i], 500, 5, len(headers_list), 20, 1))
            tasks.append(t)
            t.start()

    def trade_coin(self, headers, currency_code, side, price, amount):
        params = {"code": currency_code, "source": "PC", "side": side, "type": "LIMIT", "price": price,
                  "qty": amount, "accountType": "1004", "autoBorrow": "false"}
        resp = self.client.post(c.CoinEntrustAPI, headers=headers, data=params)
        if str(resp.status_code) == '200' and resp.json():
            print(resp.json())
            print('code: {}, side: {}, price: {}, amount: {}'.format(currency_code, side, price, amount))
        else:
            print("Error resp.status_code: {}".format(resp.status_code))

    @task
    def trade_coin_buy_XMR(self):
        for headers in headers_list:
            currency_code = "TESTL_USDT_ICNCDE_ENCRY"
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'B', str(round(_price, 2)), amount)

    @task
    def trade_coin_sell_XMR(self):
        for headers in headers_list:
            currency_code = "TESTL_USDT_ICNCDE_ENCRY"
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'S', str(round(_price, 2)), amount)


class WebsiteUser(HttpUser):
    tasks = [HttpTradeCoin]

    min_wait = 100
    max_wait = 1000
    host = "http://test.mobile.icctoro.com:7007"
