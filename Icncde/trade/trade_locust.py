# -*- encoding: utf-8 -*-
"""
@File    : trade_locust.py
@Time    : 2020/7/9 14:54
@Author  : tester
@Software: PyCharm
"""

from locust import TaskSet, HttpUser
from locust import events

from Icncde.trade import consts as c
from Icncde.trade.trade_server import TradeCoinSetUpData, get_access_token_with_headers_list

setup_trade_coin_data = TradeCoinSetUpData(c.HOST)


class HttpTradeCoin(TaskSet):

    @events.test_start.add_listener
    def on_test_start(**kwargs):
        users_headers = get_access_token_with_headers_list(c.HOST, c.EmailLoginAPI, c.Headers, c.UsernameList,
                                                           c.Password)
        #  买入的金额 小于 卖出的金额，造数据
        if setup_trade_coin_data.many_code_trade_coin(users_headers, 500, 20) is False:
            exit()


class WebsiteUser(HttpUser):
    tasks = [HttpTradeCoin]

    min_wait = 100
    max_wait = 1000
    host = "http://test.mobile.icctoro.com:7007"

# for username in c.UsernameList:
#     user_headers = get_access_token_with_headers_list(c.HOST, c.EmailLoginAPI, c.Headers, username, c.Password)
#     if trade_coin_setup_data(c.HOST + c.CoinEntrustAPI, user_headers, c.TradeCoinList, 1, 'B', 400) is False:
#         print('222222222222222')
#
# # data = c.TradeCoinList
# # for i in data:
# #     print(i.strip()+'..')
