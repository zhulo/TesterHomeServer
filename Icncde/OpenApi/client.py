# -*- encoding: utf-8 -*-
"""
@File    : client.py
@Time    : 2020/7/1 15:16
@Author  : tester
@Software: PyCharm
"""

import json

from Icncde.OpenApi import consts as c
from Icncde.OpenApi import utils as u
from common.utils.logger import Logger
from common.utils.service import HttpService

log = Logger(__name__).log()


class OpenApiRequest(HttpService):

    def __init__(self, host, api_key, api_secret_key, passphrase, use_server_time=False):
        HttpService.__init__(self, host)
        self.API_KEY = api_key
        self.API_SECRET_KEY = api_secret_key
        self.PASSPHRASE = passphrase
        self.USR_SERVER_TIME = use_server_time

    def http_request(self, method, end_point, params, param_type=c.DATA):
        json_dumps_params = json.dumps(params)
        timestamp = u.iso_local_timestamp()

        if self.USR_SERVER_TIME:
            timestamp = u.iso_server_timestamp(self.host, c.SERVER_TIMESTAMP_URL)
        sign = u.api_sign(u.api_hash(timestamp, "POST", end_point, str(json_dumps_params)), self.API_SECRET_KEY)

        header = u.header_with_sign(self.API_KEY, sign, timestamp, self.PASSPHRASE)
        response = self.request(method, end_point, header, json_dumps_params, param_type)
        return response


class OpenApi:
    def __init__(self, icc_passphrase, icc_api_key, icc_secret_key):
        self.icc_passphrase = icc_passphrase
        self.icc_api_key = icc_api_key
        self.icc_secret_key = icc_secret_key

    def header_with_params(self, method, end_point, params, use_server_time=False):
        json_dumps_param = json.dumps(params)
        timestamp = u.iso_local_timestamp()

        if use_server_time:
            timestamp = u.iso_server_timestamp(c.API_URL, c.SERVER_TIMESTAMP_URL)
        sign = u.api_sign(u.api_hash(timestamp, method.upper(), end_point, str(json_dumps_param)), self.icc_secret_key)

        header = u.header_with_sign(self.icc_api_key, sign, timestamp, self.icc_passphrase)

        return header, json_dumps_param


def header_param_without_base_info(method, end_point, params, use_server_time=False, **open_api_info):
    passphrase = open_api_info['passphrase']
    api_key = open_api_info['api_key']
    secret_key = open_api_info['secret_key']

    if passphrase and api_key and secret_key:
        json_dumps_param = json.dumps(params)
        timestamp = u.iso_local_timestamp()
        if use_server_time:
            timestamp = u.iso_server_timestamp(c.API_URL, c.SERVER_TIMESTAMP_URL)
        sign = u.api_sign(u.api_hash(timestamp, method.upper(), end_point, str(json_dumps_param)), secret_key)

        header = u.header_with_sign(api_key, sign, timestamp, passphrase)
        return header, json_dumps_param

#
# if __name__ == '__main__':
#     ic_api_key = '71f9deb815334b889a2ea5a8cd0f7ea9'
#     ic_secret_key = '5888d82d5ab94b08b7b217f1f38db498'
#     ic_passphrase = 'a111111'
#     host_ = "http://test.mobile.icctoro.com:7007"
#     orders_api = "/openapi/spot/v1/orders"
#     params_ = {'instrument_Id': "BTC_USDT_ICNCDE_ENCRY", 'side': "B", 'type': 'LIMIT', 'size': 0.01, 'price': "276"}
#     # OpenApiRequest(ic_api_key, ic_secret_key, ic_passphrase).http_request(host, "POST", orders_api, params)
#     OpenApiRequest(host_, ic_api_key, ic_secret_key, ic_passphrase).http_request("POST", orders_api, params_)
