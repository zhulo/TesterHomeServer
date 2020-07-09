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

    def __many_code_trade_coin(self, headers, side, trade_type, price, amount):
        for currency_code in c.TradeCoinList:
            currency_code = currency_code.strip()
            if self.__trade_coin(headers, currency_code, side, trade_type, price, amount) is False:
                return False

    def many_users_trade_coin(self, headers_list, side, trade_type, price, amount):
        for header in headers_list:
            if self.__many_code_trade_coin(header, side, trade_type, price, amount) is False:
                return False

    # def trade_coin_setup_data(self, end_point, headers, currency_code_list, amount, side, price):
    #     '''
    #
    #     :param end_point: end_point
    #     :param headers:
    #     :param currency_code_list:
    #     :param amount: 数量
    #     :param side: 买 B 或 卖 S
    #     :param price: 价格
    #     :return:
    #     '''
    #     for currency_code in currency_code_list:
    #         currency_code = currency_code.strip()
    #         params = {"code": currency_code, "source": "PC", "side": side, "type": "LIMIT", "price": price,
    #                   "qty": amount, "accountType": "1004", "autoBorrow": "false"}
    #         resp = requests.post(url=self.url + end_point, headers=headers, data=params)
    #         if str(resp.status_code) == '200' and resp.json():
    #             log.info(
    #                 'code: {}, side: {}, price: {}, amount: {}, response: {}'.format(currency_code, side, price, amount,
    #                                                                                  resp.json()))
    #         else:
    #             log.error("委托失败,终止测试,接口返回状态: {}, 参数: {}".format(resp.status_code, params))
    #             return False
