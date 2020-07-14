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
    def trade_coin_buy_TESTA(self):
        for headers in headers_list:
            currency_code = "TESTA_USDT_ICNCDE_ENCRY"
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'B', str(round(_price, 2)), amount)
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'S', str(round(_price, 2)), amount)

    @task
    def trade_coin_buy_TESTB(self):
        for headers in headers_list:
            currency_code = "TESTB_USDT_ICNCDE_ENCRY"
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'B', str(round(_price, 2)), amount)
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'S', str(round(_price, 2)), amount)

    @task
    def trade_coin_buy_TESTC(self):
        for headers in headers_list:
            currency_code = "TESTC_USDT_ICNCDE_ENCRY"
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'B', str(round(_price, 2)), amount)
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'S', str(round(_price, 2)), amount)

    @task
    def trade_coin_buy_TESTD(self):
        for headers in headers_list:
            currency_code = "TESTD_USDT_ICNCDE_ENCRY"
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'B', str(round(_price, 2)), amount)
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'S', str(round(_price, 2)), amount)

    @task
    def trade_coin_buy_TESTE(self):
        for headers in headers_list:
            currency_code = "TESTE_USDT_ICNCDE_ENCRY"
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'B', str(round(_price, 2)), amount)
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'S', str(round(_price, 2)), amount)

    @task
    def trade_coin_buy_TESTF(self):
        for headers in headers_list:
            currency_code = "TESTF_USDT_ICNCDE_ENCRY"
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'B', str(round(_price, 2)), amount)
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'S', str(round(_price, 2)), amount)

    @task
    def trade_coin_buy_TESTG(self):
        for headers in headers_list:
            currency_code = "TESTG_USDT_ICNCDE_ENCRY"
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'B', str(round(_price, 2)), amount)
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'S', str(round(_price, 2)), amount)

    @task
    def trade_coin_buy_TESTH(self):
        for headers in headers_list:
            currency_code = "TESTH_USDT_ICNCDE_ENCRY"
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'B', str(round(_price, 2)), amount)
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'S', str(round(_price, 2)), amount)

    @task
    def trade_coin_buy_TESTI(self):
        for headers in headers_list:
            currency_code = "TESTI_USDT_ICNCDE_ENCRY"
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'B', str(round(_price, 2)), amount)
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'S', str(round(_price, 2)), amount)

    @task
    def trade_coin_buy_TESTJ(self):
        for headers in headers_list:
            currency_code = "TESTJ_USDT_ICNCDE_ENCRY"
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'B', str(round(_price, 2)), amount)
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'S', str(round(_price, 2)), amount)

    @task
    def trade_coin_buy_TESTK(self):
        for headers in headers_list:
            currency_code = "TESTK_USDT_ICNCDE_ENCRY"
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'B', str(round(_price, 2)), amount)
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'S', str(round(_price, 2)), amount)

    @task
    def trade_coin_buy_TESTL(self):
        for headers in headers_list:
            currency_code = "TESTL_USDT_ICNCDE_ENCRY"
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'B', str(round(_price, 2)), amount)
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'S', str(round(_price, 2)), amount)

    @task
    def trade_coin_buy_TESTM(self):
        for headers in headers_list:
            currency_code = "TESTM_USDT_ICNCDE_ENCRY"
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'B', str(round(_price, 2)), amount)
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'S', str(round(_price, 2)), amount)

    @task
    def trade_coin_buy_TESTN(self):
        for headers in headers_list:
            currency_code = "TESTN_USDT_ICNCDE_ENCRY"
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'B', str(round(_price, 2)), amount)
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'S', str(round(_price, 2)), amount)

    @task
    def trade_coin_buy_TESTO(self):
        for headers in headers_list:
            currency_code = "TESTO_USDT_ICNCDE_ENCRY"
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'B', str(round(_price, 2)), amount)
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'S', str(round(_price, 2)), amount)

    @task
    def trade_coin_buy_TESTP(self):
        for headers in headers_list:
            currency_code = "TESTP_USDT_ICNCDE_ENCRY"
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'B', str(round(_price, 2)), amount)
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'S', str(round(_price, 2)), amount)

    @task
    def trade_coin_buy_TESTQ(self):
        for headers in headers_list:
            currency_code = "TESTQ_USDT_ICNCDE_ENCRY"
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'B', str(round(_price, 2)), amount)
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'S', str(round(_price, 2)), amount)

    @task
    def trade_coin_buy_TESTR(self):
        for headers in headers_list:
            currency_code = "TESTR_USDT_ICNCDE_ENCRY"
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'B', str(round(_price, 2)), amount)
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'S', str(round(_price, 2)), amount)

    @task
    def trade_coin_buy_TESTS(self):
        for headers in headers_list:
            currency_code = "TESTS_USDT_ICNCDE_ENCRY"
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'B', str(round(_price, 2)), amount)
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'S', str(round(_price, 2)), amount)

    @task
    def trade_coin_buy_TESTT(self):
        for headers in headers_list:
            currency_code = "TESTT_USDT_ICNCDE_ENCRY"
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'B', str(round(_price, 2)), amount)
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'S', str(round(_price, 2)), amount)

    @task
    def trade_coin_buy_TESTU(self):
        for headers in headers_list:
            currency_code = "TESTU_USDT_ICNCDE_ENCRY"
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'B', str(round(_price, 2)), amount)
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'S', str(round(_price, 2)), amount)

    @task
    def trade_coin_buy_TESTV(self):
        for headers in headers_list:
            currency_code = "TESTV_USDT_ICNCDE_ENCRY"
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'B', str(round(_price, 2)), amount)
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'S', str(round(_price, 2)), amount)

    @task
    def trade_coin_buy_TESTW(self):
        for headers in headers_list:
            currency_code = "TESTW_USDT_ICNCDE_ENCRY"
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'B', str(round(_price, 2)), amount)
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'S', str(round(_price, 2)), amount)

    @task
    def trade_coin_buy_TESTX(self):
        for headers in headers_list:
            currency_code = "TESTX_USDT_ICNCDE_ENCRY"
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'B', str(round(_price, 2)), amount)
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'S', str(round(_price, 2)), amount)

    @task
    def trade_coin_buy_TESTY(self):
        for headers in headers_list:
            currency_code = "TESTY_USDT_ICNCDE_ENCRY"
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'B', str(round(_price, 2)), amount)
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'S', str(round(_price, 2)), amount)

    @task
    def trade_coin_buy_TESTZ(self):
        for headers in headers_list:
            currency_code = "TESTZ_USDT_ICNCDE_ENCRY"
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'B', str(round(_price, 2)), amount)
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'S', str(round(_price, 2)), amount)

    @task
    def trade_coin_buy_ATEST(self):
        for headers in headers_list:
            currency_code = "ATEST_BTC_ICNCDE_ENCRY"
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'B', str(round(_price, 2)), amount)
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'S', str(round(_price, 2)), amount)

    @task
    def trade_coin_buy_BTEST(self):
        for headers in headers_list:
            currency_code = "BTEST_BTC_ICNCDE_ENCRY"
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'B', str(round(_price, 2)), amount)
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'S', str(round(_price, 2)), amount)

    @task
    def trade_coin_buy_CTEST(self):
        for headers in headers_list:
            currency_code = "CTEST_BTC_ICNCDE_ENCRY"
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'B', str(round(_price, 2)), amount)
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'S', str(round(_price, 2)), amount)

    @task
    def trade_coin_buy_DTEST(self):
        for headers in headers_list:
            currency_code = "DTEST_BTC_ICNCDE_ENCRY"
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'B', str(round(_price, 2)), amount)
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'S', str(round(_price, 2)), amount)

    @task
    def trade_coin_buy_ETEST(self):
        for headers in headers_list:
            currency_code = "ETEST_BTC_ICNCDE_ENCRY"
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'B', str(round(_price, 2)), amount)
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'S', str(round(_price, 2)), amount)

    @task
    def trade_coin_buy_FTEST(self):
        for headers in headers_list:
            currency_code = "FTEST_BTC_ICNCDE_ENCRY"
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'B', str(round(_price, 2)), amount)
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'S', str(round(_price, 2)), amount)

    @task
    def trade_coin_buy_GTEST(self):
        for headers in headers_list:
            currency_code = "GTEST_BTC_ICNCDE_ENCRY"
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'B', str(round(_price, 2)), amount)
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'S', str(round(_price, 2)), amount)

    @task
    def trade_coin_buy_HTEST(self):
        for headers in headers_list:
            currency_code = "HTEST_BTC_ICNCDE_ENCRY"
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'B', str(round(_price, 2)), amount)
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'S', str(round(_price, 2)), amount)

    @task
    def trade_coin_buy_ITEST(self):
        for headers in headers_list:
            currency_code = "ITEST_BTC_ICNCDE_ENCRY"
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'B', str(round(_price, 2)), amount)
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'S', str(round(_price, 2)), amount)

    @task
    def trade_coin_buy_JTEST(self):
        for headers in headers_list:
            currency_code = "JTEST_BTC_ICNCDE_ENCRY"
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'B', str(round(_price, 2)), amount)
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'S', str(round(_price, 2)), amount)

    @task
    def trade_coin_buy_KTEST(self):
        for headers in headers_list:
            currency_code = "KTEST_BTC_ICNCDE_ENCRY"
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'B', str(round(_price, 2)), amount)
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'S', str(round(_price, 2)), amount)

    @task
    def trade_coin_buy_LTEST(self):
        for headers in headers_list:
            currency_code = "LTEST_BTC_ICNCDE_ENCRY"
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'B', str(round(_price, 2)), amount)
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'S', str(round(_price, 2)), amount)

    @task
    def trade_coin_buy_MTEST(self):
        for headers in headers_list:
            currency_code = "MTEST_BTC_ICNCDE_ENCRY"
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'B', str(round(_price, 2)), amount)
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'S', str(round(_price, 2)), amount)

    @task
    def trade_coin_buy_NTEST(self):
        for headers in headers_list:
            currency_code = "NTEST_BTC_ICNCDE_ENCRY"
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'B', str(round(_price, 2)), amount)
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'S', str(round(_price, 2)), amount)

    @task
    def trade_coin_buy_OTEST(self):
        for headers in headers_list:
            currency_code = "OTEST_BTC_ICNCDE_ENCRY"
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'B', str(round(_price, 2)), amount)
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'S', str(round(_price, 2)), amount)

    @task
    def trade_coin_buy_PTEST(self):
        for headers in headers_list:
            currency_code = "PTEST_BTC_ICNCDE_ENCRY"
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'B', str(round(_price, 2)), amount)
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'S', str(round(_price, 2)), amount)

    @task
    def trade_coin_buy_QTEST(self):
        for headers in headers_list:
            currency_code = "QTEST_BTC_ICNCDE_ENCRY"
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'B', str(round(_price, 2)), amount)
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'S', str(round(_price, 2)), amount)

    @task
    def trade_coin_buy_RTEST(self):
        for headers in headers_list:
            currency_code = "RTEST_BTC_ICNCDE_ENCRY"
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'B', str(round(_price, 2)), amount)
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'S', str(round(_price, 2)), amount)

    @task
    def trade_coin_buy_STEST(self):
        for headers in headers_list:
            currency_code = "STEST_BTC_ICNCDE_ENCRY"
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'B', str(round(_price, 2)), amount)
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'S', str(round(_price, 2)), amount)

    @task
    def trade_coin_buy_TTEST(self):
        for headers in headers_list:
            currency_code = "TTEST_BTC_ICNCDE_ENCRY"
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'B', str(round(_price, 2)), amount)
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'S', str(round(_price, 2)), amount)

    @task
    def trade_coin_buy_UTEST(self):
        for headers in headers_list:
            currency_code = "UTEST_BTC_ICNCDE_ENCRY"
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'B', str(round(_price, 2)), amount)
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'S', str(round(_price, 2)), amount)

    @task
    def trade_coin_buy_VTEST(self):
        for headers in headers_list:
            currency_code = "VTEST_BTC_ICNCDE_ENCRY"
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'B', str(round(_price, 2)), amount)
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'S', str(round(_price, 2)), amount)

    @task
    def trade_coin_buy_WTEST(self):
        for headers in headers_list:
            currency_code = "WTEST_BTC_ICNCDE_ENCRY"
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'B', str(round(_price, 2)), amount)
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'S', str(round(_price, 2)), amount)

    @task
    def trade_coin_buy_XTEST(self):
        for headers in headers_list:
            currency_code = "XTEST_BTC_ICNCDE_ENCRY"
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'B', str(round(_price, 2)), amount)
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'S', str(round(_price, 2)), amount)

    @task
    def trade_coin_buy_YTEST(self):
        for headers in headers_list:
            currency_code = "YTEST_BTC_ICNCDE_ENCRY"
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'B', str(round(_price, 2)), amount)
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'S', str(round(_price, 2)), amount)

    @task
    def trade_coin_buy_ZTEST(self):
        for headers in headers_list:
            currency_code = "ZTEST_BTC_ICNCDE_ENCRY"
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'B', str(round(_price, 2)), amount)
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'S', str(round(_price, 2)), amount)


class WebsiteUser(HttpUser):
    tasks = [HttpTradeCoin]

    min_wait = 100
    max_wait = 1000
    host = "http://test.mobile.icctoro.com:7007"
