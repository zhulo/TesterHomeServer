# -*- encoding: utf-8 -*-
"""
@File    : trade_coin_test.py
@Time    : 2020/7/16 18:50
@Author  : tester
@Software: PyCharm
"""
import random

from locust import TaskSet, HttpUser, task
from locust import events

from LocustApps.locustfiles.coin import consts as c
from LocustApps.locustfiles.coin.service import reset_coin_thread, get_access_token_with_headers_list

headers_list = get_access_token_with_headers_list(c.HOST, c.EmailLoginAPI, c.Headers, c.UsernameList,
                                                  c.Password)


class HttpTradeCoin(TaskSet):

    @events.test_start.add_listener
    def on_test_start(**kwargs):
        if c.Debug is False:
            reset_coin_thread(headers_list, c.CurrencyCodeList)

    def trade_coin_transaction(self, headers, currency_code, side, operate_type, amount, price=None):
        if currency_code in c.CurrencyCodeList:
            # headers = headers_list[random.randint(0, len(headers_list) - 1)]
            side_text = "委托买入" if side == 'B' else "委托卖出"
            operate_type_text = "市价" if operate_type == 'MARKET' else "限价"

            if price is None:
                params = {"code": currency_code, "source": "PC", "side": side, "type": operate_type, "qty": amount,
                          "accountType": "1004", "autoBorrow": "false"}
            else:
                params = {"code": currency_code, "source": "PC", "side": side, "type": operate_type, "price": price,
                          "qty": amount, "accountType": "1004", "autoBorrow": "false"}
            with self.client.post(c.CoinEntrustAPI, headers=headers, data=params, catch_response=True) as response:
                if str(response.status_code) == '200':
                    try:
                        resp = response.json()
                        if resp['code'] == '200':
                            print('Pass! {}-{}-{}-{}-{}-{},resp:{} '.format(headers['user'], currency_code, side_text,
                                                                            operate_type_text, amount, price, resp))
                        else:
                            response.failure(
                                'Fail! {}-{}-{}-{}-{}-{},resp:{} '.format(headers['user'], currency_code, side_text,
                                                                          operate_type_text, amount, price, resp))
                    except Exception as e:
                        response.failure('Fail! 获取 response.json() 异常，error_msg: {}'.format(e))
                else:
                    response.failure('Fail! 请求接口失败，返回状态: {}'.format(response.status_code))
        else:
            pass

    def trade_coin_market(self, currency_code):
        if random.randint(0, 100) > 90:
            headers = headers_list[random.randint(0, len(headers_list) - 1)]
            self.trade_coin_transaction(headers, currency_code, 'B', 'MARKET', '20000')
            self.trade_coin_transaction(headers, currency_code, 'S', 'MARKET', '20000')

    def trade_coin_limit(self, currency_code):
        for headers in headers_list:
            amount, price = str(random.uniform(1, 10)), random.uniform(c.BestAsk, c.BestBid)
            self.trade_coin_transaction(headers, currency_code, 'B', 'LIMIT', amount, price)
            amount, price = str(random.uniform(1, 10)), random.uniform(c.BestAsk, c.BestBid)
            self.trade_coin_transaction(headers, currency_code, 'S', 'LIMIT', amount, price)

    def trade_coin(self, currency_code):
        self.trade_coin_limit(currency_code)
        self.trade_coin_market(currency_code)

    @task
    def trade_coin_buy_TESTA(self):
        currency_code = "TESTA_USDT_ICNCDE_ENCRY"
        self.trade_coin(currency_code)

    @task
    def trade_coin_buy_TESTB(self):
        currency_code = "TESTB_USDT_ICNCDE_ENCRY"
        self.trade_coin(currency_code)

    @task
    def trade_coin_buy_TESTC(self):
        currency_code = "TESTC_USDT_ICNCDE_ENCRY"
        self.trade_coin(currency_code)

    @task
    def trade_coin_buy_TESTD(self):
        currency_code = "TESTD_USDT_ICNCDE_ENCRY"
        self.trade_coin(currency_code)

    @task
    def trade_coin_buy_TESTE(self):
        currency_code = "TESTE_USDT_ICNCDE_ENCRY"
        self.trade_coin(currency_code)

    @task
    def trade_coin_buy_TESTF(self):
        currency_code = "TESTF_USDT_ICNCDE_ENCRY"
        self.trade_coin(currency_code)

    @task
    def trade_coin_buy_TESTG(self):
        currency_code = "TESTG_USDT_ICNCDE_ENCRY"
        self.trade_coin(currency_code)

    @task
    def trade_coin_buy_TESTH(self):
        currency_code = "TESTH_USDT_ICNCDE_ENCRY"
        self.trade_coin(currency_code)

    @task
    def trade_coin_buy_TESTI(self):
        currency_code = "TESTI_USDT_ICNCDE_ENCRY"
        self.trade_coin(currency_code)

    @task
    def trade_coin_buy_TESTJ(self):
        currency_code = "TESTJ_USDT_ICNCDE_ENCRY"
        self.trade_coin(currency_code)

    @task
    def trade_coin_buy_TESTK(self):
        currency_code = "TESTK_USDT_ICNCDE_ENCRY"
        self.trade_coin(currency_code)

    @task
    def trade_coin_buy_TESTL(self):
        currency_code = "TESTL_USDT_ICNCDE_ENCRY"
        self.trade_coin(currency_code)

    @task
    def trade_coin_buy_TESTM(self):
        currency_code = "TESTM_USDT_ICNCDE_ENCRY"
        self.trade_coin(currency_code)

    @task
    def trade_coin_buy_TESTN(self):
        currency_code = "TESTN_USDT_ICNCDE_ENCRY"
        self.trade_coin(currency_code)

    @task
    def trade_coin_buy_TESTO(self):
        currency_code = "TESTO_USDT_ICNCDE_ENCRY"
        self.trade_coin(currency_code)

    #
    # @task
    # def trade_coin_buy_TESTP(self):
    #     currency_code = "TESTP_USDT_ICNCDE_ENCRY"
    #     self.trade_coin(currency_code)
    #
    # @task
    # def trade_coin_buy_TESTQ(self):
    #     currency_code = "TESTQ_USDT_ICNCDE_ENCRY"
    #     self.trade_coin(currency_code)
    #
    # @task
    # def trade_coin_buy_TESTR(self):
    #     currency_code = "TESTR_USDT_ICNCDE_ENCRY"
    #     self.trade_coin(currency_code)
    #
    # @task
    # def trade_coin_buy_TESTS(self):
    #     currency_code = "TESTS_USDT_ICNCDE_ENCRY"
    #     self.trade_coin(currency_code)
    #
    # @task
    # def trade_coin_buy_TESTT(self):
    #     currency_code = "TESTT_USDT_ICNCDE_ENCRY"
    #     self.trade_coin(currency_code)
    #
    # @task
    # def trade_coin_buy_TESTU(self):
    #     currency_code = "TESTU_USDT_ICNCDE_ENCRY"
    #     self.trade_coin(currency_code)
    #
    # @task
    # def trade_coin_buy_TESTV(self):
    #     currency_code = "TESTV_USDT_ICNCDE_ENCRY"
    #     self.trade_coin(currency_code)
    #
    # @task
    # def trade_coin_buy_TESTW(self):
    #     currency_code = "TESTW_USDT_ICNCDE_ENCRY"
    #     self.trade_coin(currency_code)
    #
    # @task
    # def trade_coin_buy_TESTX(self):
    #     currency_code = "TESTX_USDT_ICNCDE_ENCRY"
    #     self.trade_coin(currency_code)
    #
    # @task
    # def trade_coin_buy_TESTY(self):
    #     currency_code = "TESTY_USDT_ICNCDE_ENCRY"
    #     self.trade_coin(currency_code)
    #
    # @task
    # def trade_coin_buy_TESTZ(self):
    #     currency_code = "TESTZ_USDT_ICNCDE_ENCRY"
    #     self.trade_coin(currency_code)

    @task
    def trade_coin_buy_ATEST(self):
        currency_code = "ATEST_BTC_ICNCDE_ENCRY"
        self.trade_coin(currency_code)

    @task
    def trade_coin_buy_BTEST(self):
        currency_code = "BTEST_BTC_ICNCDE_ENCRY"
        self.trade_coin(currency_code)

    @task
    def trade_coin_buy_CTEST(self):
        currency_code = "CTEST_BTC_ICNCDE_ENCRY"
        self.trade_coin(currency_code)

    @task
    def trade_coin_buy_DTEST(self):
        currency_code = "DTEST_BTC_ICNCDE_ENCRY"
        self.trade_coin(currency_code)

    @task
    def trade_coin_buy_ETEST(self):
        currency_code = "ETEST_BTC_ICNCDE_ENCRY"
        self.trade_coin(currency_code)

    @task
    def trade_coin_buy_FTEST(self):
        currency_code = "FTEST_BTC_ICNCDE_ENCRY"
        self.trade_coin(currency_code)

    @task
    def trade_coin_buy_GTEST(self):
        currency_code = "GTEST_BTC_ICNCDE_ENCRY"
        self.trade_coin(currency_code)

    @task
    def trade_coin_buy_HTEST(self):
        currency_code = "HTEST_BTC_ICNCDE_ENCRY"
        self.trade_coin(currency_code)

    @task
    def trade_coin_buy_ITEST(self):
        currency_code = "ITEST_BTC_ICNCDE_ENCRY"
        self.trade_coin(currency_code)

    @task
    def trade_coin_buy_JTEST(self):
        currency_code = "JTEST_BTC_ICNCDE_ENCRY"
        self.trade_coin(currency_code)

    @task
    def trade_coin_buy_KTEST(self):
        currency_code = "KTEST_BTC_ICNCDE_ENCRY"
        self.trade_coin(currency_code)

    @task
    def trade_coin_buy_LTEST(self):
        currency_code = "LTEST_BTC_ICNCDE_ENCRY"
        self.trade_coin(currency_code)

    @task
    def trade_coin_buy_MTEST(self):
        currency_code = "MTEST_BTC_ICNCDE_ENCRY"
        self.trade_coin(currency_code)

    @task
    def trade_coin_buy_NTEST(self):
        currency_code = "NTEST_BTC_ICNCDE_ENCRY"
        self.trade_coin(currency_code)

    @task
    def trade_coin_buy_OTEST(self):
        currency_code = "OTEST_BTC_ICNCDE_ENCRY"
        self.trade_coin(currency_code)

    # @task
    # def trade_coin_buy_PTEST(self):
    #     currency_code = "PTEST_BTC_ICNCDE_ENCRY"
    #     self.trade_coin(currency_code)
    #
    # @task
    # def trade_coin_buy_QTEST(self):
    #     currency_code = "QTEST_BTC_ICNCDE_ENCRY"
    #     self.trade_coin(currency_code)
    #
    # @task
    # def trade_coin_buy_RTEST(self):
    #     currency_code = "RTEST_BTC_ICNCDE_ENCRY"
    #     self.trade_coin(currency_code)
    #
    # @task
    # def trade_coin_buy_STEST(self):
    #     currency_code = "STEST_BTC_ICNCDE_ENCRY"
    #     self.trade_coin(currency_code)
    #
    # @task
    # def trade_coin_buy_TTEST(self):
    #     currency_code = "TTEST_BTC_ICNCDE_ENCRY"
    #     self.trade_coin(currency_code)
    #
    # @task
    # def trade_coin_buy_UTEST(self):
    #     currency_code = "UTEST_BTC_ICNCDE_ENCRY"
    #     self.trade_coin(currency_code)
    #
    # @task
    # def trade_coin_buy_VTEST(self):
    #     currency_code = "VTEST_BTC_ICNCDE_ENCRY"
    #     self.trade_coin(currency_code)
    #
    # @task
    # def trade_coin_buy_WTEST(self):
    #     currency_code = "WTEST_BTC_ICNCDE_ENCRY"
    #     self.trade_coin(currency_code)
    #
    # @task
    # def trade_coin_buy_XTEST(self):
    #     currency_code = "XTEST_BTC_ICNCDE_ENCRY"
    #     self.trade_coin(currency_code)
    #
    # @task
    # def trade_coin_buy_YTEST(self):
    #     currency_code = "YTEST_BTC_ICNCDE_ENCRY"
    #     self.trade_coin(currency_code)
    #
    # @task
    # def trade_coin_buy_ZTEST(self):
    #     currency_code = "ZTEST_BTC_ICNCDE_ENCRY"
    #     self.trade_coin(currency_code)

    @task
    def trade_coin_eth_ATEST(self):
        currency_code = "ATEST_ETH_ICNCDE_ENCRY"
        self.trade_coin(currency_code)

    @task
    def trade_coin_eth_TESTA(self):
        currency_code = "TESTA_ETH_ICNCDE_ENCRY"
        self.trade_coin(currency_code)


class WebsiteUser(HttpUser):
    tasks = [HttpTradeCoin]

    min_wait = c.MinWait
    max_wait = c.MaxWait
    host = "http://test.mobile.icctoro.com:7007"
