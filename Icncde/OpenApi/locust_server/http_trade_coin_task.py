# -*- encoding: utf-8 -*-
"""
@File    : http_trade_coin_task.py
@Time    : 2020/7/3 11:03
@Author  : tester
@Software: PyCharm
"""
import random

import requests
from locust import TaskSet, task, HttpUser
from locust import events

host = "http://test.mobile.icctoro.com:7007"

api_login = "/api/user/login/email"
api_coin_entrust = "/api/coin/entrust"

headers = {"Accept": "application/json", "Content-Language": "zh-cn", "Source-Site": "pc.jys", "userId": "",
           "Content-Type": "application/x-www-form-urlencoded", "Authorization": ""}
best_ask = 200
best_bid = 300


class HttpTradeCoin(TaskSet):

    @events.test_start.add_listener
    def on_test_start(**kwargs):
        param = {"loginName": "open0001@qq.com", "password": "6846860684f05029abccc09a53cd66f1",
                 "validCodeType": "email", "deviceName": "web", "resolution": "1920x1080", "softwareVersion": "1.0.0",
                 "deviceVersion": ""}
        resp = requests.post(url=host + api_login, headers=headers, data=param)
        if str(resp.status_code) == "200" and resp.json():
            response = resp.json()
            access_token = response['data']['accessToken']
            headers['Authorization'] = access_token

    def trade_coin(self, currency_code, side, price, amount):
        params = {"code": currency_code, "source": "PC", "side": side, "type": "LIMIT", "price": price,
                  "qty": amount, "accountType": "1004", "autoBorrow": "false"}
        resp = self.client.post(api_coin_entrust, headers=headers, data=params)
        # assert str(resp.status_code) == '200'
        if str(resp.status_code) == '200' and resp.json():
            print(resp.json())
            print('code: {}, side: {}, price: {}, amount: {}'.format(currency_code, side, price, amount))
        else:
            print("Error resp.status_code: {}".format(resp.status_code))

    @task
    def trade_coin_buy_TESTA(self):
        currency_code = "TESTA_USDT_ICNCDE_ENCRY"
        _price = random.uniform(best_ask, best_bid)  # 卖出的价格
        amount = str(random.uniform(1, 10))
        self.trade_coin(currency_code, 'B', str(round(_price, 2)), amount)

    @task
    def trade_coin_sell_TESTA(self):
        currency_code = "TESTA_USDT_ICNCDE_ENCRY"
        _price = random.uniform(best_ask, best_bid)  # 卖出的价格
        amount = str(random.uniform(1, 10))
        self.trade_coin(currency_code, 'S', str(round(_price, 2)), amount)

    @task
    def trade_coin_buy_TESTB(self):
        currency_code = "TESTB_USDT_ICNCDE_ENCRY"
        _price = random.uniform(best_ask, best_bid)  # 卖出的价格
        amount = str(random.uniform(1, 10))
        self.trade_coin(currency_code, 'B', str(round(_price, 2)), amount)

    @task
    def trade_coin_sell_TESTB(self):
        currency_code = "TESTB_USDT_ICNCDE_ENCRY"
        _price = random.uniform(best_ask, best_bid)  # 卖出的价格
        amount = str(random.uniform(1, 10))
        self.trade_coin(currency_code, 'S', str(round(_price, 2)), amount)

    @task
    def trade_coin_buy_TESTC(self):
        currency_code = "TESTC_USDT_ICNCDE_ENCRY"
        _price = random.uniform(best_ask, best_bid)  # 卖出的价格
        amount = str(random.uniform(1, 10))
        self.trade_coin(currency_code, 'B', str(round(_price, 2)), amount)

    @task
    def trade_coin_sell_TESTC(self):
        currency_code = "TESTC_USDT_ICNCDE_ENCRY"
        _price = random.uniform(best_ask, best_bid)  # 卖出的价格
        amount = str(random.uniform(1, 10))
        self.trade_coin(currency_code, 'S', str(round(_price, 2)), amount)

    @task
    def trade_coin_buy_TESTD(self):
        currency_code = "TESTD_USDT_ICNCDE_ENCRY"
        _price = random.uniform(best_ask, best_bid)  # 卖出的价格
        amount = str(random.uniform(1, 10))
        self.trade_coin(currency_code, 'B', str(round(_price, 2)), amount)

    @task
    def trade_coin_sell_TESTD(self):
        currency_code = "TESTD_USDT_ICNCDE_ENCRY"
        _price = random.uniform(best_ask, best_bid)  # 卖出的价格
        amount = str(random.uniform(1, 10))
        self.trade_coin(currency_code, 'S', str(round(_price, 2)), amount)

    @task
    def trade_coin_buy_TESTE(self):
        currency_code = "TESTE_USDT_ICNCDE_ENCRY"
        _price = random.uniform(best_ask, best_bid)  # 卖出的价格
        amount = str(random.uniform(1, 10))
        self.trade_coin(currency_code, 'B', str(round(_price, 2)), amount)

    @task
    def trade_coin_sell_TESTE(self):
        currency_code = "TESTE_USDT_ICNCDE_ENCRY"
        _price = random.uniform(best_ask, best_bid)  # 卖出的价格
        amount = str(random.uniform(1, 10))
        self.trade_coin(currency_code, 'S', str(round(_price, 2)), amount)

    @task
    def trade_coin_buy_TESTF(self):
        currency_code = "TESTF_USDT_ICNCDE_ENCRY"
        _price = random.uniform(best_ask, best_bid)  # 卖出的价格
        amount = str(random.uniform(1, 10))
        self.trade_coin(currency_code, 'B', str(round(_price, 2)), amount)

    @task
    def trade_coin_sell_TESTF(self):
        currency_code = "TESTF_USDT_ICNCDE_ENCRY"
        _price = random.uniform(best_ask, best_bid)  # 卖出的价格
        amount = str(random.uniform(1, 10))
        self.trade_coin(currency_code, 'S', str(round(_price, 2)), amount)

    @task
    def trade_coin_buy_TESTG(self):
        currency_code = "TESTG_USDT_ICNCDE_ENCRY"
        _price = random.uniform(best_ask, best_bid)  # 卖出的价格
        amount = str(random.uniform(1, 10))
        self.trade_coin(currency_code, 'B', str(round(_price, 2)), amount)

    @task
    def trade_coin_sell_TESTG(self):
        currency_code = "TESTG_USDT_ICNCDE_ENCRY"
        _price = random.uniform(best_ask, best_bid)  # 卖出的价格
        amount = str(random.uniform(1, 10))
        self.trade_coin(currency_code, 'S', str(round(_price, 2)), amount)

    @task
    def trade_coin_buy_TESTH(self):
        currency_code = "TESTH_USDT_ICNCDE_ENCRY"
        _price = random.uniform(best_ask, best_bid)  # 卖出的价格
        amount = str(random.uniform(1, 10))
        self.trade_coin(currency_code, 'B', str(round(_price, 2)), amount)

    @task
    def trade_coin_sell_TESTH(self):
        currency_code = "TESTH_USDT_ICNCDE_ENCRY"
        _price = random.uniform(best_ask, best_bid)  # 卖出的价格
        amount = str(random.uniform(1, 10))
        self.trade_coin(currency_code, 'S', str(round(_price, 2)), amount)

    @task
    def trade_coin_buy_TESTI(self):
        currency_code = "TESTI_USDT_ICNCDE_ENCRY"
        _price = random.uniform(best_ask, best_bid)  # 卖出的价格
        amount = str(random.uniform(1, 10))
        self.trade_coin(currency_code, 'B', str(round(_price, 2)), amount)

    @task
    def trade_coin_sell_TESTI(self):
        currency_code = "TESTI_USDT_ICNCDE_ENCRY"
        _price = random.uniform(best_ask, best_bid)  # 卖出的价格
        amount = str(random.uniform(1, 10))
        self.trade_coin(currency_code, 'S', str(round(_price, 2)), amount)

    @task
    def trade_coin_buy_TESTJ(self):
        currency_code = "TESTJ_USDT_ICNCDE_ENCRY"
        _price = random.uniform(best_ask, best_bid)  # 卖出的价格
        amount = str(random.uniform(1, 10))
        self.trade_coin(currency_code, 'B', str(round(_price, 2)), amount)

    @task
    def trade_coin_sell_TESTJ(self):
        currency_code = "TESTJ_USDT_ICNCDE_ENCRY"
        _price = random.uniform(best_ask, best_bid)  # 卖出的价格
        amount = str(random.uniform(1, 10))
        self.trade_coin(currency_code, 'S', str(round(_price, 2)), amount)

    @task
    def trade_coin_buy_TESTK(self):
        currency_code = "TESTK_USDT_ICNCDE_ENCRY"
        _price = random.uniform(best_ask, best_bid)  # 卖出的价格
        amount = str(random.uniform(1, 10))
        self.trade_coin(currency_code, 'B', str(round(_price, 2)), amount)

    @task
    def trade_coin_sell_TESTK(self):
        currency_code = "TESTK_USDT_ICNCDE_ENCRY"
        _price = random.uniform(best_ask, best_bid)  # 卖出的价格
        amount = str(random.uniform(1, 10))
        self.trade_coin(currency_code, 'S', str(round(_price, 2)), amount)

    @task
    def trade_coin_buy_TESTL(self):
        currency_code = "TESTL_USDT_ICNCDE_ENCRY"
        _price = random.uniform(best_ask, best_bid)  # 卖出的价格
        amount = str(random.uniform(1, 10))
        self.trade_coin(currency_code, 'B', str(round(_price, 2)), amount)

    @task
    def trade_coin_sell_TESTL(self):
        currency_code = "TESTL_USDT_ICNCDE_ENCRY"
        _price = random.uniform(best_ask, best_bid)  # 卖出的价格
        amount = str(random.uniform(1, 10))
        self.trade_coin(currency_code, 'S', str(round(_price, 2)), amount)

    @task
    def trade_coin_buy_TESTM(self):
        currency_code = "TESTM_USDT_ICNCDE_ENCRY"
        _price = random.uniform(best_ask, best_bid)  # 卖出的价格
        amount = str(random.uniform(1, 10))
        self.trade_coin(currency_code, 'B', str(round(_price, 2)), amount)

    @task
    def trade_coin_sell_TESTM(self):
        currency_code = "TESTM_USDT_ICNCDE_ENCRY"
        _price = random.uniform(best_ask, best_bid)  # 卖出的价格
        amount = str(random.uniform(1, 10))
        self.trade_coin(currency_code, 'S', str(round(_price, 2)), amount)

    @task
    def trade_coin_buy_TESTN(self):
        currency_code = "TESTN_USDT_ICNCDE_ENCRY"
        _price = random.uniform(best_ask, best_bid)  # 卖出的价格
        amount = str(random.uniform(1, 10))
        self.trade_coin(currency_code, 'B', str(round(_price, 2)), amount)

    @task
    def trade_coin_sell_TESTN(self):
        currency_code = "TESTN_USDT_ICNCDE_ENCRY"
        _price = random.uniform(best_ask, best_bid)  # 卖出的价格
        amount = str(random.uniform(1, 10))
        self.trade_coin(currency_code, 'S', str(round(_price, 2)), amount)

    @task
    def trade_coin_buy_TESTO(self):
        currency_code = "TESTO_USDT_ICNCDE_ENCRY"
        _price = random.uniform(best_ask, best_bid)  # 卖出的价格
        amount = str(random.uniform(1, 10))
        self.trade_coin(currency_code, 'B', str(round(_price, 2)), amount)

    @task
    def trade_coin_sell_TESTO(self):
        currency_code = "TESTO_USDT_ICNCDE_ENCRY"
        _price = random.uniform(best_ask, best_bid)  # 卖出的价格
        amount = str(random.uniform(1, 10))
        self.trade_coin(currency_code, 'S', str(round(_price, 2)), amount)

    @task
    def trade_coin_buy_TESTP(self):
        currency_code = "TESTP_USDT_ICNCDE_ENCRY"
        _price = random.uniform(best_ask, best_bid)  # 卖出的价格
        amount = str(random.uniform(1, 10))
        self.trade_coin(currency_code, 'B', str(round(_price, 2)), amount)

    @task
    def trade_coin_sell_TESTP(self):
        currency_code = "TESTP_USDT_ICNCDE_ENCRY"
        _price = random.uniform(best_ask, best_bid)  # 卖出的价格
        amount = str(random.uniform(1, 10))
        self.trade_coin(currency_code, 'S', str(round(_price, 2)), amount)

    # ==============
    @task
    def trade_coin_buy_TESTQ(self):
        currency_code = "TESTQ_USDT_ICNCDE_ENCRY"
        _price = random.uniform(best_ask, best_bid)  # 卖出的价格
        amount = str(random.uniform(1, 10))
        self.trade_coin(currency_code, 'B', str(round(_price, 2)), amount)

    @task
    def trade_coin_sell_TESTQ(self):
        currency_code = "TESTQ_USDT_ICNCDE_ENCRY"
        _price = random.uniform(best_ask, best_bid)  # 卖出的价格
        amount = str(random.uniform(1, 10))
        self.trade_coin(currency_code, 'S', str(round(_price, 2)), amount)

    @task
    def trade_coin_buy_TESTR(self):
        currency_code = "TESTR_USDT_ICNCDE_ENCRY"
        _price = random.uniform(best_ask, best_bid)  # 卖出的价格
        amount = str(random.uniform(1, 10))
        self.trade_coin(currency_code, 'B', str(round(_price, 2)), amount)

    @task
    def trade_coin_sell_TESTR(self):
        currency_code = "TESTR_USDT_ICNCDE_ENCRY"
        _price = random.uniform(best_ask, best_bid)  # 卖出的价格
        amount = str(random.uniform(1, 10))
        self.trade_coin(currency_code, 'S', str(round(_price, 2)), amount)

    @task
    def trade_coin_buy_TESTS(self):
        currency_code = "TESTS_USDT_ICNCDE_ENCRY"
        _price = random.uniform(best_ask, best_bid)  # 卖出的价格
        amount = str(random.uniform(1, 10))
        self.trade_coin(currency_code, 'B', str(round(_price, 2)), amount)

    @task
    def trade_coin_sell_TESTS(self):
        currency_code = "TESTS_USDT_ICNCDE_ENCRY"
        _price = random.uniform(best_ask, best_bid)  # 卖出的价格
        amount = str(random.uniform(1, 10))
        self.trade_coin(currency_code, 'S', str(round(_price, 2)), amount)

    @task
    def trade_coin_buy_TESTT(self):
        currency_code = "TESTT_USDT_ICNCDE_ENCRY"
        _price = random.uniform(best_ask, best_bid)  # 卖出的价格
        amount = str(random.uniform(1, 10))
        self.trade_coin(currency_code, 'B', str(round(_price, 2)), amount)

    @task
    def trade_coin_sell_TESTT(self):
        currency_code = "TESTT_USDT_ICNCDE_ENCRY"
        _price = random.uniform(best_ask, best_bid)  # 卖出的价格
        amount = str(random.uniform(1, 10))
        self.trade_coin(currency_code, 'S', str(round(_price, 2)), amount)

    @task
    def trade_coin_buy_TESTU(self):
        currency_code = "TESTU_USDT_ICNCDE_ENCRY"
        _price = random.uniform(best_ask, best_bid)  # 卖出的价格
        amount = str(random.uniform(1, 10))
        self.trade_coin(currency_code, 'B', str(round(_price, 2)), amount)

    @task
    def trade_coin_sell_TESTU(self):
        currency_code = "TESTU_USDT_ICNCDE_ENCRY"
        _price = random.uniform(best_ask, best_bid)  # 卖出的价格
        amount = str(random.uniform(1, 10))
        self.trade_coin(currency_code, 'S', str(round(_price, 2)), amount)

    @task
    def trade_coin_buy_TESTV(self):
        currency_code = "TESTV_USDT_ICNCDE_ENCRY"
        _price = random.uniform(best_ask, best_bid)  # 卖出的价格
        amount = str(random.uniform(1, 10))
        self.trade_coin(currency_code, 'B', str(round(_price, 2)), amount)

    @task
    def trade_coin_sell_TESTV(self):
        currency_code = "TESTV_USDT_ICNCDE_ENCRY"
        _price = random.uniform(best_ask, best_bid)  # 卖出的价格
        amount = str(random.uniform(1, 10))
        self.trade_coin(currency_code, 'S', str(round(_price, 2)), amount)

    @task
    def trade_coin_buy_TESTW(self):
        currency_code = "TESTW_USDT_ICNCDE_ENCRY"
        _price = random.uniform(best_ask, best_bid)  # 卖出的价格
        amount = str(random.uniform(1, 10))
        self.trade_coin(currency_code, 'B', str(round(_price, 2)), amount)

    @task
    def trade_coin_sell_TESTW(self):
        currency_code = "TESTW_USDT_ICNCDE_ENCRY"
        _price = random.uniform(best_ask, best_bid)  # 卖出的价格
        amount = str(random.uniform(1, 10))
        self.trade_coin(currency_code, 'S', str(round(_price, 2)), amount)

    @task
    def trade_coin_buy_TESTX(self):
        currency_code = "TESTX_USDT_ICNCDE_ENCRY"
        _price = random.uniform(best_ask, best_bid)  # 卖出的价格
        amount = str(random.uniform(1, 10))
        self.trade_coin(currency_code, 'B', str(round(_price, 2)), amount)

    @task
    def trade_coin_sell_TESTX(self):
        currency_code = "TESTX_USDT_ICNCDE_ENCRY"
        _price = random.uniform(best_ask, best_bid)  # 卖出的价格
        amount = str(random.uniform(1, 10))
        self.trade_coin(currency_code, 'S', str(round(_price, 2)), amount)

    @task
    def trade_coin_buy_TESTY(self):
        currency_code = "TESTY_USDT_ICNCDE_ENCRY"
        _price = random.uniform(best_ask, best_bid)  # 卖出的价格
        amount = str(random.uniform(1, 10))
        self.trade_coin(currency_code, 'B', str(round(_price, 2)), amount)

    @task
    def trade_coin_sell_TESTY(self):
        currency_code = "TESTY_USDT_ICNCDE_ENCRY"
        _price = random.uniform(best_ask, best_bid)  # 卖出的价格
        amount = str(random.uniform(1, 10))
        self.trade_coin(currency_code, 'S', str(round(_price, 2)), amount)

    @task
    def trade_coin_buy_TESTZ(self):
        currency_code = "TESTZ_USDT_ICNCDE_ENCRY"
        _price = random.uniform(best_ask, best_bid)  # 卖出的价格
        amount = str(random.uniform(1, 10))
        self.trade_coin(currency_code, 'B', str(round(_price, 2)), amount)

    @task
    def trade_coin_sell_TESTZ(self):
        currency_code = "TESTZ_USDT_ICNCDE_ENCRY"
        _price = random.uniform(best_ask, best_bid)  # 卖出的价格
        amount = str(random.uniform(1, 10))
        self.trade_coin(currency_code, 'S', str(round(_price, 2)), amount)


class WebsiteUser(HttpUser):
    tasks = [HttpTradeCoin]
    min_wait = 100
    max_wait = 1000
    host = "http://test.mobile.icctoro.com:7007"
