# -*- encoding: utf-8 -*-
"""
@File    : trade_server.py
@Time    : 2020/7/2 11:41
@Author  : tester
@Software: PyCharm
"""
import copy
import threading

import requests

from Icncde.trade import consts as c
from common.utils.logger import Logger

log = Logger(__name__).log()


def get_access_token_with_headers_list(host, api, headers, username, password: str):
    if isinstance(username, list):
        users_headers = []
        for user in username:
            params = {"loginName": user, "password": password, "validCodeType": "email", "deviceName": "web",
                      "resolution": "1920x1080", "softwareVersion": "1.0.0", "deviceVersion": ""}
            resp = requests.post(url=host + api, headers=headers, data=params)
            if str(resp.status_code) == "200" and resp.json():
                response = resp.json()
                access_token = response['data']['accessToken']
                headers = copy.deepcopy(headers)
                headers['Authorization'] = access_token
                headers['user'] = user
                log.info('获取到用户 {} 的 headers: {}'.format(user, headers))
                users_headers.append(headers)
            else:
                log.error('获取用户 {} accessToken异常，终止测试'.format(username))
                return False
        return users_headers
    else:
        params = {"loginName": username, "password": password, "validCodeType": "email", "deviceName": "web",
                  "resolution": "1920x1080", "softwareVersion": "1.0.0", "deviceVersion": ""}
        resp = requests.post(url=host + api, headers=headers, data=params)
        if str(resp.status_code) == "200" and resp.json():
            response = resp.json()
            access_token = response['data']['accessToken']
            headers['Authorization'] = access_token
            log.info('获取到用户 {} 的 headers: {}'.format(username, headers))
            return headers
        else:
            log.error('获取用户 {} accessToken异常，终止测试'.format(username))
            return False


class TradeCoinSetUpData:
    def __init__(self, url):
        self.url = url

    def one_headers_trade_coin(self, headers, initial_price, trade_coin_num, user_num, trade_highly, amount):
        '''
        创建盘口深度
        1.获取所有trade code
        2.每个用户进行限价委托 买 和 卖， 买入的盘1价格 始终 小于卖1价格
        :param headers:
        :param initial_price: 初始买入卖出价格
        :param trade_coin_num: 单个盘口的总委托数
        :param user_num: 用户总数
        :param trade_highly: 单个币对的盘口深度
        :param amount: 单个委托单的委托数量
        :return:
        '''
        log.info("开始造数据，初始盘口默认值: %s" % str(initial_price))
        best_ask = initial_price - 10  # 买入初始价  即卖出盘1
        best_bid = initial_price + 10  # 卖出初始价  即卖出盘1
        #  单个用户需要委托的订单数
        user_trade_request_times = int(int(trade_coin_num) / int(user_num))
        log.info('{} 个用户需要对单个盘口进行委托的总量为: {}，当前 {} 用户需要创建的委托量(购买和卖出分别等于)： {}'.format(user_num, trade_coin_num,
                                                                                    headers['user'],
                                                                                    user_trade_request_times))
        # 深度 trade highly
        for currency_code in c.TradeCoinList:
            currency_code = currency_code.strip()
            log.info('获取到当前币对: {}, 开始进行单个币对的盘口深度 {} 进行造数据'.format(currency_code, trade_highly))
            for highly in range(trade_highly):
                if self.__set_coin_trade_entrust_amount(user_trade_request_times, headers, currency_code, best_ask,
                                                        best_bid, amount) is False:
                    return False
                best_ask -= 1
                best_bid += 1

    def __trade_coin(self, headers, currency_code, side, trade_type, price, amount):
        '''
        :param headers: 带有 access_token 的headers
        :param currency_code:
        :param side: B 买入 、S 卖出
        :param trade_type: "LIMIT" == 限价买入
        :param price: 价格
        :param amount: 数量
        :return:
        '''
        params = {"code": currency_code, "source": "PC", "side": side, "type": trade_type, "price": price,
                  "qty": amount, "accountType": "1004", "autoBorrow": "false"}
        resp = requests.post(url=self.url + c.CoinEntrustAPI, headers=headers, data=params)
        if str(resp.status_code) == '200' and resp.json():
            log.info(
                'code: {}, side: {}, price: {}, amount: {}, response: {}'.format(currency_code, side, price, amount,
                                                                                 resp.json()))
        else:
            log.error("委托失败,终止测试,接口返回状态: {}, 参数: {}".format(resp.status_code, params))
            return False

    # def many_code_trade_coin(self, headers_list, initial_price, trade_highly):
    #     '''
    #     创建盘口深度
    #     1.获取所有trade code
    #     2.每个用户进行限价委托 买 和 卖， 买入的盘1价格 始终 小于卖1价格
    #     :param headers_list:
    #     :param initial_price:
    #     :param trade_coin_num: 单个盘口的总委托数
    #     :param trade_highly: 单个盘口的总委托数
    #     :return:
    #     '''
    #     log.info("开始造数据，初始盘口默认值: %s" % str(initial_price))
    #     best_ask = initial_price - 10  # 买入初始价  即卖出盘1
    #     best_bid = initial_price + 10  # 卖出初始价  即卖出盘1
    #     # 深度 trade highly
    #     for currency_code in c.TradeCoinList:
    #         currency_code = currency_code.strip()
    #         for highly in range(trade_highly):
    #             #  单个用户需要委托的订单数
    #             user_trade_request_times = int(200 / len(headers_list))
    #             for headers in headers_list:
    #                 if self.set_coin_trade_entrust_amount(user_trade_request_times, headers, currency_code, best_ask,
    #                                                       best_bid) is False:
    #                     return False
    #             best_ask -= 1
    #             best_bid += 1

    def __set_coin_trade_entrust_amount(self, num, headers, currency_code, best_ask, best_bid, amount):
        '''
        单个盘口委托买和卖分别N次
        :param num:  单个盘口委托的总量
        :param headers:
        :param currency_code:
        :param best_ask:
        :param best_bid:
        :param amount:
        :return:
        '''
        log.info('用户 {},开始对单个币对 {} 进行买入和卖出的委托总量 {} 造数据'.format(headers['user'], currency_code, num))
        for i in range(num):
            if self.__trade_coin(headers, currency_code, 'B', 'LIMIT', best_ask, amount) is False:
                return False
            # 卖出
            if self.__trade_coin(headers, currency_code, 'S', 'LIMIT', best_bid, amount) is False:
                return False


headers_list = get_access_token_with_headers_list(c.HOST, c.EmailLoginAPI, c.Headers, c.UsernameList,
                                                  c.Password)
# from pprint import pprint
#
# pprint(headers_list)

if __name__ == '__main__':
    tasks = []
    for i in range(len(headers_list)):
        # :param headers:
        # :param initial_price: 初始买入卖出价格
        # :param trade_coin_num: 单个盘口的总委托数
        # :param user_num: 用户总数
        # :param trade_highly: 单个币对的盘口深度
        # :param amount: 单个委托单的委托数量
        print(headers_list[i])
        t = threading.Thread(target=TradeCoinSetUpData(c.HOST).one_headers_trade_coin,
                             args=(headers_list[i], 200, 5, len(headers_list), 5, 1))
        tasks.append(t)
        t.start()
