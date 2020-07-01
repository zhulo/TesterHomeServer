# -*- encoding: utf-8 -*-
"""
@File    : consts.py
@Time    : 2020/6/29 10:47
@Author  : tester
@Software: PyCharm
"""

# http header
# API_URL = 'http://www.icncde.com'
API_URL = 'http://test.mobile.icctoro.com:7007'
CONTENT_TYPE = 'Content-Type'
ICC_ACCESS_KEY = 'ICC-ACCESS-KEY'
ICC_ACCESS_SIGN = 'ICC-ACCESS-SIGN'
ICC_ACCESS_TIMESTAMP = 'ICC-ACCESS-TIMESTAMP'
ICC_ACCESS_PASSPHRASE = 'ICC-ACCESS-PASSPHRASE'

ACCEPT = 'Accept'
COOKIE = 'Cookie'
LOCALE = 'Locale='

APPLICATION_JSON = 'application/json'

GET = "GET"
POST = "POST"
DATA = "DATA"
DELETE = "DELETE"

ConstsAsk = 5000
ConstsBid = 5000

SERVER_TIMESTAMP_URL = '/openapi/general/v1/time'

# spot
SPOT_ACCOUNT_INFO = '/openapi/spot/v1/accounts/'
SPOT_COIN_ACCOUNT_INFO = '/openapi/spot/v1/accounts/'
SPOT_ORDER = '/openapi/spot/v1/orders'  # 币币下单
SPOT_REVOKE_ORDER = '/openapi/spot/v1/cancel_orders/'
SPOT_REVOKE_ORDERS = '/openapi/spot/v1/cancel_batch_orders/'
SPOT_SPECIFIC_TICKER = '/openapi/spot/v1/instruments/'
SPOT_ORDERS_PENDING = '/openapi/spot/v1/orders_pending'


class OpenApiAccount:
    open_api_user_001 = {"email": "open0001@qq.com", "passphrase": "a111111",
                         "api_key": "a2cf0345aa4e4de480207e995afb069e",
                         "secret_key": "0105fdcf24c14a54b7dbe46153bbf505"}
    open_api_user_002 = {"email": "open0002@qq.com", "passphrase": "a111111",
                         "api_key": "f743a963cf854f948ced7b3930664924",
                         "secret_key": "2e458b826af245feb814b9642a805acd"}
    open_api_user_003 = {"email": "open0003@qq.com", "passphrase": "a111111",
                         "api_key": "2fe47a00a440430c9eb03ab138207217",
                         "secret_key": "1bbee10febe4460fbab751176ea714c2"}
    open_api_user_004 = {"email": "open0004@qq.com", "passphrase": "a111111",
                         "api_key": "b520a71d44c64c4186748e593fae52d5",
                         "secret_key": "c02c724fd1ba4ded9904cc11d7d915fe"}
    open_api_user_005 = {"email": "open0005@qq.com", "passphrase": "a111111",
                         "api_key": "eeab036f8ba6475692bb9a0a71155fc6",
                         "secret_key": "fe4351a91ceb44fda7b02098e0755498"}


class CurrencyInfo:
    currency_code = "DSSJ_USDT_ICNCDE_ENCRY"
    best_ask = 100
    best_bid = 1000


class DataBaseConfig:
    database_config = {"host": "10.10.23.99", "user": "dssj", "password": "dssj@DSSJ123"}
