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
