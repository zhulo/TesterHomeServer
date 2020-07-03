# -*- encoding: utf-8 -*-
"""
@File    : locsuts_bak.py
@Time    : 2020/7/1 19:51
@Author  : tester
@Software: PyCharm
"""

import random

import requests
from locust import TaskSet, task, HttpUser

from Icncde.OpenApi.client import header_param_without_base_info
from common.utils.logger import Logger
from common.utils.service import DataBaseService

log = Logger(__name__).log()

username = "open0005@qq.com"
icc_host = 'http://test.mobile.icctoro.com:7007'
ic_api_key = '5d0397f363784f47bd9d87a06c12679c'
ic_secret_key = 'c55dd86200c043b0a16dc464b0d797cc'
ic_passphrase = 'a111111'

open_user_001 = {"email": "open0005@qq.com", "passphrase": "a111111", "api_key": "eeab036f8ba6475692bb9a0a71155fc6",
         "secret_key": "fe4351a91ceb44fda7b02098e0755498"}
# api = OpenApi(ic_passphrase, ic_api_key, ic_secret_key)
database_config = {"host": "10.10.23.99", "user": "dssj", "password": "dssj@DSSJ123"}

instrument_id = "DSSJ_USDT_ICNCDE_ENCRY"
best_ask, best_bid = 5000, 10000


class InitCoinOrder(object):

    def cancel_order(self, order_id):
        '''
        撤销指定订单
        :param order_id:
        :return:
        '''
        end_point = "/openapi/spot/v1/cancel_orders/{}".format(order_id)
        params = {'orderId': str(order_id)}
        # header, param_to_str = api.header_with_params("POST", end_point, params, use_server_time=False)

        header, param_to_str = header_param_without_base_info("POST", end_point, params, use_server_time=False,
                                                              **open_user_001)

        resp = requests.post(url='http://test.mobile.icctoro.com:7007' + end_point, headers=header, data=param_to_str)
        log.info(resp.status_code)
        log.info(resp.text)

    def get_ticker(self):
        instrument_id = "TESTA_USDT_ICNCDE_ENCRY"
        end_point = '/openapi/spot/v1/instruments/' + str(instrument_id) + '/ticker'
        # header, params = api.header_with_params("GET", end_point, {}, use_server_time=False)
        header, params = header_param_without_base_info("GET", end_point, {}, use_server_time=False, **open_user_001)
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
        sql = "select id from icc_trade_coin.coin_orders where user_id = {} and status = 0".format(
            self.get_user_id())
        order_with_id_list = DataBaseService(database_config).query(sql, False)
        if len(order_with_id_list) > 0:
            for o in order_with_id_list:
                self.cancel_order(o['id'])
            log.info('---' * 100)
            log.info('---' * 100)
            log.info('---' * 100)
        else:
            return None


if __name__ == '__main__':
    InitCoinOrder().cancel_coin_order()


class OpenApiTest(TaskSet):
    # from locust import events
    #
    # @events.test_start.add_listener
    # def on_test_start(**kwargs):
    #     '''
    #     固定设置一个买入的价格
    #     instrumentId 币对,如：DSSJ_USDT_ICNCDE_ENCRY
    #     side 买卖类型：B-买 S-卖
    #     type LIMIT-限价 MARKET-市价
    #     size 买入或卖出的数量
    #     price 限价单（价格）必填
    #     :return:
    #     '''
    #     InitCoinOrder().cancel_coin_order()
    #     # instrument_id = "DSSJ_USDT_ICNCDE_ENCRY"
    #     # end_point = '/openapi/spot/v1/orders'
    #     # params = {'instrument_Id': instrument_id, 'side': 'B', 'type': 'LIMIT', 'size': '10000',
    #     #           'price': '1000'}
    #     # header, param = api.header_with_params("POST", end_point, params, use_server_time=False)
    #     # resp = requests.post(icc_host + end_point, headers=header, data=param)
    #     # log.info(resp.json())

    @task(1)
    def taker_order_with_sell_01(self):
        sell_value = round(random.uniform(best_ask, best_bid), 2)
        end_point = '/openapi/spot/v1/orders'
        params = {'instrument_Id': instrument_id, 'side': 'S', 'type': 'LIMIT', 'size': '0.01',
                  'price': str(sell_value)}
        # header, param = api.header_with_params("POST", end_point, params, use_server_time=False)
        header, param = header_param_without_base_info("POST", end_point, params, use_server_time=False,
                                                       **open_user_001)
        resp = self.client.post(end_point, headers=header, data=param)

        log.info("用户: {}, 下单卖出价格： {}, 接口返回： {}".format(open_user_001['email'], sell_value, resp.json()))

        sell_value = sell_value + random.randint(20, 30)
        params = {'instrument_Id': instrument_id, 'side': 'B', 'type': 'LIMIT', 'size': '0.01',
                  'price': str(sell_value + 1)}
        # header, param = api.header_with_params("POST", end_point, params, use_server_time=False)
        header, param = header_param_without_base_info("POST", end_point, params, use_server_time=False,
                                                       **open_user_001)
        resp = self.client.post(end_point, headers=header, data=param)
        log.info("用户: {}, 下单买入价格： {}, 接口返回： {}".format(open_user_001['email'], sell_value, resp.json()))

    @task(1)
    def taker_order_with_sell_02(self):
        sell_value = round(random.uniform(best_ask, best_bid), 2)
        end_point = '/openapi/spot/v1/orders'
        params = {'instrument_Id': instrument_id, 'side': 'S', 'type': 'LIMIT', 'size': '0.01',
                  'price': str(sell_value)}
        # header, param = api.header_with_params("POST", end_point, params, use_server_time=False)
        header, param = header_param_without_base_info("POST", end_point, params, use_server_time=False,
                                                       **open_user_001)
        resp = self.client.post(end_point, headers=header, data=param)

        log.info("用户: {}, 下单卖出价格： {}, 接口返回： {}".format(open_user_001['email'], sell_value, resp.json()))

        sell_value = sell_value + random.randint(20, 30)
        params = {'instrument_Id': instrument_id, 'side': 'B', 'type': 'LIMIT', 'size': '0.01',
                  'price': str(sell_value + 1)}
        # header, param = api.header_with_params("POST", end_point, params, use_server_time=False)
        header, param = header_param_without_base_info("POST", end_point, params, use_server_time=False,
                                                       **open_user_001)
        resp = self.client.post(end_point, headers=header, data=param)
        log.info("用户: {}, 下单买入价格： {}, 接口返回： {}".format(open_user_001['email'], sell_value, resp.json()))


class WebsiteUser(HttpUser):
    tasks = [OpenApiTest]
    min_wait = 100
    max_wait = 10000
    host = icc_host
