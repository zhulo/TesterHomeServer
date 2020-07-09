# -*- encoding: utf-8 -*-
"""
@File    : consts.py
@Time    : 2020/7/2 11:51
@Author  : tester
@Software: PyCharm
"""

HOST = "http://test.mobile.icctoro.com:7007"
EmailLoginAPI = "/api/user/login/email"
CoinEntrustAPI = "/api/coin/entrust"

Password = '6846860684f05029abccc09a53cd66f1'  # 默认登录账号密码

Headers = {"Accept": "application/json", "Content-Language": "zh-cn", "Source-Site": "pc.jys", "userId": "",
           "Content-Type": "application/x-www-form-urlencoded", "Authorization": ""}

UsernameList = ['open0001@qq.com', 'open0002@qq.com', 'open0003@qq.com', 'open0004@qq.com', 'open0005@qq.com']

BestAsk = 200
BestBid = 500


# UserHeadersList = get_access_token(HOST, EmailLoginAPI, Headers, UsernameList, Password)

def load_trade_coin_list():
    from TesterHomeServer.settings import BASE_DIR
    file_path = BASE_DIR + r'\Icncde\trade\trade_coin_info.txt'
    with open(file_path, "r") as f:
        data = f.readlines()
        return data


TradeCoinList = load_trade_coin_list()
