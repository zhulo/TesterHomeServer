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
best_ask = 350
best_bid = 650
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
                                 args=(headers_list[i], 500, 20, len(headers_list), 50, 1))
            tasks.append(t)
            t.start()

    def trade_coin(self, headers, currency_code, side, price, amount):
        '''
        限价买入 卖出
        :param headers:
        :param currency_code:
        :param side:
        :param price:
        :param amount:
        :return:
        '''
        params = {"code": currency_code, "source": "PC", "side": side, "type": "LIMIT", "price": price,
                  "qty": amount, "accountType": "1004", "autoBorrow": "false"}
        resp = self.client.post(c.CoinEntrustAPI, headers=headers, data=params)
        if str(resp.status_code) == '200' and resp.json():
            _side = '买入' if side == 'B' else '卖出'
            print('限价委托 {}, resp={} '.format(_side, resp.json()))
        else:
            print("Error resp.status_code: {}".format(resp.status_code))

    def trade_coin_market(self, headers_list, currency_code):
        '''
        市价买入 卖出
        :param headers:
        :param currency_code:
        :param side:
        :return:
        '''
        headers = headers_list[random.randint(0, len(headers_list) - 1)]
        buy_params = {"code": currency_code, "source": "PC", "side": 'B', "type": "MARKET",
                      "qty": '20000', "accountType": "1004", "autoBorrow": "false"}
        buy_resp = self.client.post(c.CoinEntrustAPI, headers=headers, data=buy_params)
        if str(buy_resp.status_code) == '200' and buy_resp.json():
            print('市价委托 买入, resp={} '.format(buy_resp.json()))

        sell_params = {"code": currency_code, "source": "PC", "side": 'S', "type": "MARKET",
                       "qty": '20000', "accountType": "1004", "autoBorrow": "false"}
        sell_resp = self.client.post(c.CoinEntrustAPI, headers=headers, data=sell_params)
        if str(sell_resp.status_code) == '200' and sell_resp.json():
            print('市价委托 卖出, resp={} '.format(sell_resp.json()))

    @task
    def trade_coin_buy_TESTA(self):
        currency_code = "TESTA_USDT_ICNCDE_ENCRY"
        for headers in headers_list:
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'B', str(round(_price, 2)), amount)
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'S', str(round(_price, 2)), amount)
        self.trade_coin_market(headers_list, currency_code)

    @task
    def trade_coin_buy_TESTB(self):
        currency_code = "TESTB_USDT_ICNCDE_ENCRY"
        for headers in headers_list:
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'B', str(round(_price, 2)), amount)
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'S', str(round(_price, 2)), amount)
        self.trade_coin_market(headers_list, currency_code)

    @task
    def trade_coin_buy_TESTC(self):
        currency_code = "TESTC_USDT_ICNCDE_ENCRY"
        for headers in headers_list:
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'B', str(round(_price, 2)), amount)
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'S', str(round(_price, 2)), amount)
        self.trade_coin_market(headers_list, currency_code)

    @task
    def trade_coin_buy_TESTD(self):
        currency_code = "TESTD_USDT_ICNCDE_ENCRY"
        for headers in headers_list:
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'B', str(round(_price, 2)), amount)
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'S', str(round(_price, 2)), amount)
        self.trade_coin_market(headers_list, currency_code)

    @task
    def trade_coin_buy_TESTE(self):
        currency_code = "TESTE_USDT_ICNCDE_ENCRY"
        for headers in headers_list:
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'B', str(round(_price, 2)), amount)
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'S', str(round(_price, 2)), amount)
        self.trade_coin_market(headers_list, currency_code)

    @task
    def trade_coin_buy_TESTF(self):
        currency_code = "TESTF_USDT_ICNCDE_ENCRY"
        for headers in headers_list:
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'B', str(round(_price, 2)), amount)
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'S', str(round(_price, 2)), amount)
        self.trade_coin_market(headers_list, currency_code)

    @task
    def trade_coin_buy_TESTG(self):
        currency_code = "TESTG_USDT_ICNCDE_ENCRY"
        for headers in headers_list:
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'B', str(round(_price, 2)), amount)
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'S', str(round(_price, 2)), amount)
        self.trade_coin_market(headers_list, currency_code)

    @task
    def trade_coin_buy_TESTH(self):
        currency_code = "TESTH_USDT_ICNCDE_ENCRY"
        for headers in headers_list:
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'B', str(round(_price, 2)), amount)
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'S', str(round(_price, 2)), amount)
        self.trade_coin_market(headers_list, currency_code)

    @task
    def trade_coin_buy_TESTI(self):
        currency_code = "TESTI_USDT_ICNCDE_ENCRY"
        for headers in headers_list:
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'B', str(round(_price, 2)), amount)
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'S', str(round(_price, 2)), amount)
        self.trade_coin_market(headers_list, currency_code)

    @task
    def trade_coin_buy_TESTJ(self):
        currency_code = "TESTJ_USDT_ICNCDE_ENCRY"
        for headers in headers_list:
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'B', str(round(_price, 2)), amount)
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'S', str(round(_price, 2)), amount)
        self.trade_coin_market(headers_list, currency_code)

    @task
    def trade_coin_buy_TESTK(self):
        currency_code = "TESTK_USDT_ICNCDE_ENCRY"
        for headers in headers_list:
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'B', str(round(_price, 2)), amount)
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'S', str(round(_price, 2)), amount)
        self.trade_coin_market(headers_list, currency_code)

    @task
    def trade_coin_buy_TESTL(self):
        currency_code = "TESTL_USDT_ICNCDE_ENCRY"
        for headers in headers_list:
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'B', str(round(_price, 2)), amount)
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'S', str(round(_price, 2)), amount)
        self.trade_coin_market(headers_list, currency_code)

    @task
    def trade_coin_buy_TESTM(self):
        currency_code = "TESTM_USDT_ICNCDE_ENCRY"
        for headers in headers_list:
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'B', str(round(_price, 2)), amount)
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'S', str(round(_price, 2)), amount)
        self.trade_coin_market(headers_list, currency_code)

    @task
    def trade_coin_buy_TESTN(self):
        currency_code = "TESTN_USDT_ICNCDE_ENCRY"
        for headers in headers_list:
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'B', str(round(_price, 2)), amount)
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'S', str(round(_price, 2)), amount)
        self.trade_coin_market(headers_list, currency_code)

    @task
    def trade_coin_buy_TESTO(self):
        currency_code = "TESTO_USDT_ICNCDE_ENCRY"
        for headers in headers_list:
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'B', str(round(_price, 2)), amount)
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'S', str(round(_price, 2)), amount)
        self.trade_coin_market(headers_list, currency_code)

    @task
    def trade_coin_buy_TESTP(self):
        currency_code = "TESTP_USDT_ICNCDE_ENCRY"
        for headers in headers_list:
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'B', str(round(_price, 2)), amount)
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'S', str(round(_price, 2)), amount)
        self.trade_coin_market(headers_list, currency_code)

    @task
    def trade_coin_buy_TESTQ(self):
        currency_code = "TESTQ_USDT_ICNCDE_ENCRY"
        for headers in headers_list:
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'B', str(round(_price, 2)), amount)
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'S', str(round(_price, 2)), amount)
        self.trade_coin_market(headers_list, currency_code)

    @task
    def trade_coin_buy_TESTR(self):
        currency_code = "TESTR_USDT_ICNCDE_ENCRY"
        for headers in headers_list:
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'B', str(round(_price, 2)), amount)
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'S', str(round(_price, 2)), amount)
        self.trade_coin_market(headers_list, currency_code)

    @task
    def trade_coin_buy_TESTS(self):
        currency_code = "TESTS_USDT_ICNCDE_ENCRY"
        for headers in headers_list:
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'B', str(round(_price, 2)), amount)
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'S', str(round(_price, 2)), amount)
        self.trade_coin_market(headers_list, currency_code)

    @task
    def trade_coin_buy_TESTT(self):
        currency_code = "TESTT_USDT_ICNCDE_ENCRY"
        for headers in headers_list:
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'B', str(round(_price, 2)), amount)
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'S', str(round(_price, 2)), amount)
        self.trade_coin_market(headers_list, currency_code)

    @task
    def trade_coin_buy_TESTU(self):
        currency_code = "TESTU_USDT_ICNCDE_ENCRY"
        for headers in headers_list:
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'B', str(round(_price, 2)), amount)
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'S', str(round(_price, 2)), amount)
        self.trade_coin_market(headers_list, currency_code)

    @task
    def trade_coin_buy_TESTV(self):
        currency_code = "TESTV_USDT_ICNCDE_ENCRY"
        for headers in headers_list:
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'B', str(round(_price, 2)), amount)
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'S', str(round(_price, 2)), amount)
        self.trade_coin_market(headers_list, currency_code)

    @task
    def trade_coin_buy_TESTW(self):
        currency_code = "TESTW_USDT_ICNCDE_ENCRY"
        for headers in headers_list:
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'B', str(round(_price, 2)), amount)
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'S', str(round(_price, 2)), amount)
        self.trade_coin_market(headers_list, currency_code)

    @task
    def trade_coin_buy_TESTX(self):
        currency_code = "TESTX_USDT_ICNCDE_ENCRY"
        for headers in headers_list:
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'B', str(round(_price, 2)), amount)
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'S', str(round(_price, 2)), amount)
        self.trade_coin_market(headers_list, currency_code)

    @task
    def trade_coin_buy_TESTY(self):
        currency_code = "TESTY_USDT_ICNCDE_ENCRY"
        for headers in headers_list:
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'B', str(round(_price, 2)), amount)
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'S', str(round(_price, 2)), amount)
        self.trade_coin_market(headers_list, currency_code)

    @task
    def trade_coin_buy_TESTZ(self):
        currency_code = "TESTZ_USDT_ICNCDE_ENCRY"
        for headers in headers_list:
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'B', str(round(_price, 2)), amount)
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'S', str(round(_price, 2)), amount)
        self.trade_coin_market(headers_list, currency_code)

    @task
    def trade_coin_buy_ATEST(self):
        currency_code = "ATEST_BTC_ICNCDE_ENCRY"
        for headers in headers_list:
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'B', str(round(_price, 2)), amount)
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'S', str(round(_price, 2)), amount)
        self.trade_coin_market(headers_list, currency_code)

    @task
    def trade_coin_buy_BTEST(self):
        currency_code = "BTEST_BTC_ICNCDE_ENCRY"
        for headers in headers_list:
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'B', str(round(_price, 2)), amount)
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'S', str(round(_price, 2)), amount)
        self.trade_coin_market(headers_list, currency_code)

    @task
    def trade_coin_buy_CTEST(self):
        currency_code = "CTEST_BTC_ICNCDE_ENCRY"
        for headers in headers_list:
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'B', str(round(_price, 2)), amount)
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'S', str(round(_price, 2)), amount)
        self.trade_coin_market(headers_list, currency_code)

    @task
    def trade_coin_buy_DTEST(self):
        currency_code = "DTEST_BTC_ICNCDE_ENCRY"
        for headers in headers_list:
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'B', str(round(_price, 2)), amount)
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'S', str(round(_price, 2)), amount)
        self.trade_coin_market(headers_list, currency_code)

    @task
    def trade_coin_buy_ETEST(self):
        currency_code = "ETEST_BTC_ICNCDE_ENCRY"
        for headers in headers_list:
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'B', str(round(_price, 2)), amount)
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'S', str(round(_price, 2)), amount)
        self.trade_coin_market(headers_list, currency_code)

    @task
    def trade_coin_buy_FTEST(self):
        currency_code = "FTEST_BTC_ICNCDE_ENCRY"
        for headers in headers_list:
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'B', str(round(_price, 2)), amount)
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'S', str(round(_price, 2)), amount)
        self.trade_coin_market(headers_list, currency_code)

    @task
    def trade_coin_buy_GTEST(self):
        currency_code = "GTEST_BTC_ICNCDE_ENCRY"
        for headers in headers_list:
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'B', str(round(_price, 2)), amount)
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'S', str(round(_price, 2)), amount)
        self.trade_coin_market(headers_list, currency_code)

    @task
    def trade_coin_buy_HTEST(self):
        currency_code = "HTEST_BTC_ICNCDE_ENCRY"
        for headers in headers_list:
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'B', str(round(_price, 2)), amount)
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'S', str(round(_price, 2)), amount)
        self.trade_coin_market(headers_list, currency_code)

    @task
    def trade_coin_buy_ITEST(self):
        currency_code = "ITEST_BTC_ICNCDE_ENCRY"
        for headers in headers_list:
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'B', str(round(_price, 2)), amount)
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'S', str(round(_price, 2)), amount)
        self.trade_coin_market(headers_list, currency_code)

    @task
    def trade_coin_buy_JTEST(self):
        currency_code = "JTEST_BTC_ICNCDE_ENCRY"
        for headers in headers_list:
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'B', str(round(_price, 2)), amount)
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'S', str(round(_price, 2)), amount)
        self.trade_coin_market(headers_list, currency_code)

    @task
    def trade_coin_buy_KTEST(self):
        currency_code = "KTEST_BTC_ICNCDE_ENCRY"
        for headers in headers_list:
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'B', str(round(_price, 2)), amount)
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'S', str(round(_price, 2)), amount)
        self.trade_coin_market(headers_list, currency_code)

    @task
    def trade_coin_buy_LTEST(self):
        currency_code = "LTEST_BTC_ICNCDE_ENCRY"
        for headers in headers_list:
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'B', str(round(_price, 2)), amount)
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'S', str(round(_price, 2)), amount)
        self.trade_coin_market(headers_list, currency_code)

    @task
    def trade_coin_buy_MTEST(self):
        currency_code = "MTEST_BTC_ICNCDE_ENCRY"
        for headers in headers_list:
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'B', str(round(_price, 2)), amount)
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'S', str(round(_price, 2)), amount)
        self.trade_coin_market(headers_list, currency_code)

    @task
    def trade_coin_buy_NTEST(self):
        currency_code = "NTEST_BTC_ICNCDE_ENCRY"
        for headers in headers_list:
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'B', str(round(_price, 2)), amount)
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'S', str(round(_price, 2)), amount)
        self.trade_coin_market(headers_list, currency_code)

    @task
    def trade_coin_buy_OTEST(self):
        currency_code = "OTEST_BTC_ICNCDE_ENCRY"
        for headers in headers_list:
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'B', str(round(_price, 2)), amount)
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'S', str(round(_price, 2)), amount)
        self.trade_coin_market(headers_list, currency_code)

    @task
    def trade_coin_buy_PTEST(self):
        currency_code = "PTEST_BTC_ICNCDE_ENCRY"
        for headers in headers_list:
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'B', str(round(_price, 2)), amount)
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'S', str(round(_price, 2)), amount)
        self.trade_coin_market(headers_list, currency_code)

    @task
    def trade_coin_buy_QTEST(self):
        currency_code = "QTEST_BTC_ICNCDE_ENCRY"
        for headers in headers_list:
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'B', str(round(_price, 2)), amount)
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'S', str(round(_price, 2)), amount)
        self.trade_coin_market(headers_list, currency_code)

    @task
    def trade_coin_buy_RTEST(self):
        currency_code = "RTEST_BTC_ICNCDE_ENCRY"
        for headers in headers_list:
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'B', str(round(_price, 2)), amount)
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'S', str(round(_price, 2)), amount)
        self.trade_coin_market(headers_list, currency_code)

    @task
    def trade_coin_buy_STEST(self):
        currency_code = "STEST_BTC_ICNCDE_ENCRY"
        for headers in headers_list:
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'B', str(round(_price, 2)), amount)
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'S', str(round(_price, 2)), amount)
        self.trade_coin_market(headers_list, currency_code)

    @task
    def trade_coin_buy_TTEST(self):
        currency_code = "TTEST_BTC_ICNCDE_ENCRY"
        for headers in headers_list:
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'B', str(round(_price, 2)), amount)
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'S', str(round(_price, 2)), amount)
        self.trade_coin_market(headers_list, currency_code)

    @task
    def trade_coin_buy_UTEST(self):
        currency_code = "UTEST_BTC_ICNCDE_ENCRY"
        for headers in headers_list:
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'B', str(round(_price, 2)), amount)
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'S', str(round(_price, 2)), amount)
        self.trade_coin_market(headers_list, currency_code)

    @task
    def trade_coin_buy_VTEST(self):
        currency_code = "VTEST_BTC_ICNCDE_ENCRY"
        for headers in headers_list:
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'B', str(round(_price, 2)), amount)
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'S', str(round(_price, 2)), amount)
        self.trade_coin_market(headers_list, currency_code)

    @task
    def trade_coin_buy_WTEST(self):
        currency_code = "WTEST_BTC_ICNCDE_ENCRY"
        for headers in headers_list:
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'B', str(round(_price, 2)), amount)
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'S', str(round(_price, 2)), amount)
        self.trade_coin_market(headers_list, currency_code)

    @task
    def trade_coin_buy_XTEST(self):
        currency_code = "XTEST_BTC_ICNCDE_ENCRY"
        for headers in headers_list:
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'B', str(round(_price, 2)), amount)
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'S', str(round(_price, 2)), amount)
        self.trade_coin_market(headers_list, currency_code)

    @task
    def trade_coin_buy_YTEST(self):
        currency_code = "YTEST_BTC_ICNCDE_ENCRY"
        for headers in headers_list:
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'B', str(round(_price, 2)), amount)
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'S', str(round(_price, 2)), amount)
        self.trade_coin_market(headers_list, currency_code)

    @task
    def trade_coin_buy_ZTEST(self):
        currency_code = "ZTEST_BTC_ICNCDE_ENCRY"
        for headers in headers_list:
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'B', str(round(_price, 2)), amount)
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'S', str(round(_price, 2)), amount)
        self.trade_coin_market(headers_list, currency_code)

    @task
    def trade_coin_eth_ATEST(self):
        currency_code = "ATEST_ETH_ICNCDE_ENCRY"
        for headers in headers_list:
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'B', str(round(_price, 2)), amount)
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'S', str(round(_price, 2)), amount)
        self.trade_coin_market(headers_list, currency_code)

    @task
    def trade_coin_eth_TESTA(self):
        currency_code = "TESTA_ETH_ICNCDE_ENCRY"
        for headers in headers_list:
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'B', str(round(_price, 2)), amount)
            _price = random.uniform(best_ask, best_bid)  # 卖出的价格
            amount = str(random.uniform(1, 10))
            self.trade_coin(headers, currency_code, 'S', str(round(_price, 2)), amount)
        self.trade_coin_market(headers_list, currency_code)


class WebsiteUser(HttpUser):
    tasks = [HttpTradeCoin]

    min_wait = 100
    max_wait = 1000
    host = "http://test.mobile.icctoro.com:7007"
