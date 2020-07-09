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
        if setup_trade_coin_data.many_users_trade_coin(users_headers, 'B', 'LIMIT', 500, 1) is False:  # 加上卖 金额在某个范围内要递增
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
