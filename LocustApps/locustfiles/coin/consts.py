HOST = "http://test.mobile.icctoro.com:7007"
EmailLoginAPI = "/api/user/login/email"
CoinEntrustAPI = "/api/coin/entrust"

Password = '6846860684f05029abccc09a53cd66f1'  # 默认登录账号密码

Headers = {"Accept": "application/json", "Content-Language": "zh-cn", "Source-Site": "pc.jys", "userId": "",
           "Content-Type": "application/x-www-form-urlencoded", "Authorization": ""}

UsernameList = ['open0001@qq.com', 'open0002@qq.com', 'open0003@qq.com', 'open0004@qq.com', 'open0005@qq.com']

# CurrencyCodeList = [
#     'TESTA_USDT_ICNCDE_ENCRY', 'TESTB_USDT_ICNCDE_ENCRY', 'TESTC_USDT_ICNCDE_ENCRY', 'TESTD_USDT_ICNCDE_ENCRY',
#     'TESTE_USDT_ICNCDE_ENCRY', 'TESTF_USDT_ICNCDE_ENCRY', 'TESTG_USDT_ICNCDE_ENCRY', 'TESTH_USDT_ICNCDE_ENCRY',
#     'TESTI_USDT_ICNCDE_ENCRY', 'TESTJ_USDT_ICNCDE_ENCRY', 'TESTK_USDT_ICNCDE_ENCRY', 'TESTL_USDT_ICNCDE_ENCRY',
#     'TESTM_USDT_ICNCDE_ENCRY', 'TESTN_USDT_ICNCDE_ENCRY', 'TESTO_USDT_ICNCDE_ENCRY', 'ATEST_BTC_ICNCDE_ENCRY',
#     'CTEST_BTC_ICNCDE_ENCRY', 'BTEST_BTC_ICNCDE_ENCRY', 'DTEST_BTC_ICNCDE_ENCRY', 'ETEST_BTC_ICNCDE_ENCRY',
#     'FTEST_BTC_ICNCDE_ENCRY', 'GTEST_BTC_ICNCDE_ENCRY', 'HTEST_BTC_ICNCDE_ENCRY', 'ITEST_BTC_ICNCDE_ENCRY',
#     'JTEST_BTC_ICNCDE_ENCRY', 'KTEST_BTC_ICNCDE_ENCRY', 'LTEST_BTC_ICNCDE_ENCRY', 'MTEST_BTC_ICNCDE_ENCRY',
#     'NTEST_BTC_ICNCDE_ENCRY', 'OTEST_BTC_ICNCDE_ENCRY', 'TESTA_ETH_ICNCDE_ENCRY', 'ATEST_ETH_ICNCDE_ENCRY'
# ]


CurrencyCodeList = [
    'TESTX_USDT_ICNCDE_ENCRY', 'TESTL_USDT_ICNCDE_ENCRY', 'TESTI_USDT_ICNCDE_ENCRY', 'TESTQ_USDT_ICNCDE_ENCRY']

'''造数据初始条件'''
CoinHeightNums = 50  # 盘口高度 深度
OrdersNums = 50  # 单个盘口的委托数
InitPrice = 500  # 初始价格

'''委托订单进行撮合初始条件'''
BestAsk = 200
BestBid = 500
