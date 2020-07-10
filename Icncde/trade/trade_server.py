# -*- encoding: utf-8 -*-
"""
@File    : trade_server.py
@Time    : 2020/7/2 11:41
@Author  : tester
@Software: PyCharm
"""
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
                headers['Authorization'] = access_token
                log.info('获取到用户 {} 的 headers: {}'.format(username, headers))
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

    def many_code_trade_coin(self, headers_list, initial_price, trade_highly):
        '''
        创建盘口深度
        1.获取所有trade code
        2.每个用户进行限价委托 买 和 卖， 买入的盘1价格 始终 小于卖1价格
        :param headers_list:
        :param initial_price:
        :param trade_coin_num: 单个盘口的总委托数
        :param trade_highly: 单个盘口的总委托数
        :return:
        '''
        log.info("开始造数据，初始盘口默认值: %s" % str(initial_price))
        best_ask = initial_price - 10  # 买入初始价  即卖出盘1
        best_bid = initial_price + 10  # 卖出初始价  即卖出盘1
        # 深度 trade highly
        for currency_code in c.TradeCoinList:
            currency_code = currency_code.strip()
            for highly in range(trade_highly):
                #  单个用户需要委托的订单数
                user_trade_request_times = int(200 / len(headers_list))
                for headers in headers_list:
                    if self.set_coin_trade_entrust_amount(user_trade_request_times, headers, currency_code, best_ask,
                                                          best_bid) is False:
                        return False
                best_ask -= 1
                best_bid += 1

    def set_coin_trade_entrust_amount(self, num, headers, currency_code, best_ask, best_bid):
        '''
        :param num:  单个盘口委托的总量
        :param headers:
        :param currency_code:
        :param best_ask:
        :param best_bid:
        :return:
        '''
        for i in range(num):
            if self.__trade_coin(headers, currency_code, 'B', 'LIMIT', best_ask, 1) is False:
                return False
            # 卖出
            if self.__trade_coin(headers, currency_code, 'S', 'LIMIT', best_bid, 1) is False:
                return False
