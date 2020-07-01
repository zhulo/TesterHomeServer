# -*- encoding: utf-8 -*-
"""
@File    : icc_open_api.py
@Time    : 2020/6/30 9:51
@Author  : tester
@Software: PyCharm
"""
import random
import requests
from locust import TaskSet, task, HttpUser
from locust import events

from IccBank.ICC.client import OpenApi
from common.utils.logger import Logger
from common.utils.service import DataBaseService

log = Logger(__name__).log()

username = "testerhome@qq.com"
icc_host = 'http://test.mobile.icctoro.com:7007'
ic_api_key = '5d0397f363784f47bd9d87a06c12679c'
ic_secret_key = 'c55dd86200c043b0a16dc464b0d797cc'
ic_passphrase = 'a111111'

api = OpenApi(ic_passphrase, ic_api_key, ic_secret_key)
database_config = {"host": "10.10.23.99", "user": "dssj", "password": "dssj@DSSJ123"}


class InitCoinOrder(object):

    def cancel_order(self, order_id):
        '''
        撤销指定订单
        :param order_id:
        :return:
        '''
        end_point = "/openapi/spot/v1/cancel_orders/{}".format(order_id)
        params = {'orderId': str(order_id)}
        header, param_to_str = api.header_with_params("POST", end_point, params, use_server_time=False)
        resp = requests.post(url=icc_host + end_point, headers=header, data=param_to_str)
        log.info(resp.status_code)
        log.info(resp.text)

    def get_ticker(self):
        instrument_id = "BTC_USDT_ICNCDE_ENCRY"
        end_point = '/openapi/spot/v1/instruments/' + str(instrument_id) + '/ticker'
        header, params = api.header_with_params("GET", end_point, {}, use_server_time=False)
        resp = requests.get(end_point, headers=header)
        log.info(resp.json())

    def get_user_id(self):
        sql = '''select id from icc_user.user_base_info where email = "{}"'''.format(username)
        user_id = DataBaseService(database_config).query(sql, True)
        return user_id['id']

    def cancel_coin_order(self):
        '''
        获取当前账户所有的未成交的卖出/买入委托订单；判断coin 冻结资金是否等于0
        status = 0 撮合中，即未成交
        side = 方向: 0-买 1-卖
        :return:
        '''
        sql = "select id from icc_trade_coin.coin_orders where user_id = {} and status = 0".format(self.get_user_id())
        order_with_id_list = DataBaseService(database_config).query(sql, False)
        if len(order_with_id_list) > 0:
            for o in order_with_id_list:
                self.cancel_order(o['id'])


if __name__ == '__main__':
    InitCoinOrder().cancel_coin_order()


class OpenApiTest(TaskSet):

    @events.test_start.add_listener
    def on_test_start(**kwargs):
        '''
        固定设置一个买入的价格
        instrumentId 币对,如：BTC_USDT_ICNCDE_ENCRY
        side 买卖类型：B-买 S-卖
        type LIMIT-限价 MARKET-市价
        size 买入或卖出的数量
        price 限价单（价格）必填
        :return:
        '''
        instrument_id = "BTC_USDT_ICNCDE_ENCRY"
        end_point = '/openapi/spot/v1/orders'
        params = {'instrument_Id': instrument_id, 'side': 'B', 'type': 'LIMIT', 'size': '10000',
                  'price': '1000'}
        header, param = api.header_with_params("POST", end_point, params, use_server_time=False)
        resp = requests.post(icc_host + end_point, headers=header, data=param)
        log.info(resp.json())

    @task(1)
    def taker_order_with_sell(self):
        '''
        买入
        :return:
        '''
        # instrument_id = "BTC_USDT_ICNCDE_ENCRY"
        # end_point = '/openapi/spot/v1/instruments/' + str(instrument_id) + '/ticker'
        # header, params = api.header_with_params("GET", end_point, {}, use_server_time=False)
        # response = self.client.get(end_point, headers=header)
        # resp = response.json()
        # log.info("获取到最新的成交价格: {}".format(resp))

        # best_ask, best_bid = float(10000.90) + float(1000), float(1000.60) - float(100)
        # best_ask, best_bid = float(resp['bestAsk']), float(resp['bestBid'])
        # if int(best_ask) == 0 or int(best_bid) == 0:

        best_ask, best_bid = 5000, 10000
        sell_value = round(random.uniform(best_ask, best_bid), 2)
        instrument_id = "BTC_USDT_ICNCDE_ENCRY"
        end_point = '/openapi/spot/v1/orders'
        params = {'instrument_Id': instrument_id, 'side': 'S', 'type': 'LIMIT', 'size': '0.01',
                  'price': str(sell_value)}
        header, param = api.header_with_params("POST", end_point, params, use_server_time=False)
        resp = self.client.post(end_point, headers=header, data=param)
        log.info("卖出实时匹配买入 {}".format(resp.json()))

        params = {'instrument_Id': instrument_id, 'side': 'B', 'type': 'LIMIT', 'size': '0.01',
                  'price': str(sell_value + 1)}
        header, param = api.header_with_params("POST", end_point, params, use_server_time=False)
        self.client.post(end_point, headers=header, data=param)

    # @events.test_stop.add_listener
    # def on_test_stop(**kwargs):
    #     print("A new test is ending")


class WebsiteUser(HttpUser):
    tasks = [OpenApiTest]
    min_wait = 100
    max_wait = 10000
    host = icc_host
