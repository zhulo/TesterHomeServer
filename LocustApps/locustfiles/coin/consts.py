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
# 1045571974178123776
# 1045572121007005696
# 1045572218784620544
# 1045572306604957696
# 1045572397119156224

BestAsk = 200
BestBid = 500


# UserHeadersList = get_access_token(HOST, EmailLoginAPI, Headers, UsernameList, Password)

def load_trade_coin_list():
    currency_code_list = []
    from TesterHomeServer.settings import BASE_DIR
    file_path = BASE_DIR + r'/Icncde/trade/trade_coin_info.txt'
    with open(file_path, "r") as f:
        code_list = f.readlines()
    for code in code_list:
        currency_code_list.append(code.strip())
    return currency_code_list


TradeCoinList = ['TESTA_USDT_ICNCDE_ENCRY', 'TESTB_USDT_ICNCDE_ENCRY', 'TESTC_USDT_ICNCDE_ENCRY',
                 'TESTD_USDT_ICNCDE_ENCRY', 'TESTE_USDT_ICNCDE_ENCRY', 'TESTF_USDT_ICNCDE_ENCRY',
                 'TESTG_USDT_ICNCDE_ENCRY', 'TESTH_USDT_ICNCDE_ENCRY', 'TESTI_USDT_ICNCDE_ENCRY',
                 'TESTJ_USDT_ICNCDE_ENCRY', 'TESTK_USDT_ICNCDE_ENCRY', 'TESTL_USDT_ICNCDE_ENCRY',
                 'TESTM_USDT_ICNCDE_ENCRY', 'TESTN_USDT_ICNCDE_ENCRY', 'TESTO_USDT_ICNCDE_ENCRY',
                 'ATEST_BTC_ICNCDE_ENCRY', 'CTEST_BTC_ICNCDE_ENCRY', 'BTEST_BTC_ICNCDE_ENCRY', 'DTEST_BTC_ICNCDE_ENCRY',
                 'ETEST_BTC_ICNCDE_ENCRY', 'FTEST_BTC_ICNCDE_ENCRY', 'GTEST_BTC_ICNCDE_ENCRY', 'HTEST_BTC_ICNCDE_ENCRY',
                 'ITEST_BTC_ICNCDE_ENCRY', 'JTEST_BTC_ICNCDE_ENCRY', 'KTEST_BTC_ICNCDE_ENCRY', 'LTEST_BTC_ICNCDE_ENCRY',
                 'MTEST_BTC_ICNCDE_ENCRY', 'NTEST_BTC_ICNCDE_ENCRY', 'OTEST_BTC_ICNCDE_ENCRY', 'TESTA_ETH_ICNCDE_ENCRY',
                 'ATEST_ETH_ICNCDE_ENCRY']
import random
n = 0
for i in range(1, 100):
    num = random.randint(0, 100)
    if num > 80:
        print(num)
        n += 1

print('--------')
print(n)