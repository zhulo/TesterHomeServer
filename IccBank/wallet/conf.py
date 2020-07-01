private_key_pem = b"""
-----BEGIN RSA PRIVATE KEY-----
MIICdQIBADANBgkqhkiG9w0BAQEFAASCAl8wggJbAgEAAoGBAItA9ivffijUqaG3vXFBmvBuQoUtGTHHWIbpVwDVCJYVWmNhkUBvbygLJtaV7C+oolKPZtq9ucYZrlb7r15P/RBVvMt8X7GiN8wHmOv+hLw8kD8GXH3nk1MyywrCIpRsDRf++p5QWbFiCW3yLRcYMz4Z6Y1+KHzb6X4q7jeXwI9pAgMBAAECgYAxFL1vaz9xLrt3N2a7E2+DzKj/fYzCwctPCdFThsKW+4G3Q31Jo70e9QdEXOU5SwujY83RzUs8KnMLT3xZFoJQBkwxLfWCbICsDS/r/84AdThu8fjlHgJCC7rj8hJKy2106c/gCisejhxekLxN/ivr0XtsCdNZNzKpw/Gy37wY3QJBAOsAAYryk4FAYmRK8f6kAZOK7V4urpT+UCO/Ncc0OMD+ccajkBEVBQtUCjjLkMKivjjftc0klWorasug0oZvTz8CQQCXspwPE3RDfPQS6HISpuhaFGaWdZ0m8fkpeq9dp0ZhoZ/sD1oeeQJIYSGR9gwkUFHNvaHFb7o+LQZ58KgRrB9XAkBFJddOX1pv6dYJ1NOoLfIYzARUdkAAr2Q9YIIef4tDnpsz6+T0Yc7+Klhnpd6Opvx6F7mTB3S/rM7b5BKOZCpZAkAur1gZx6nrLyRKQWEB3n35YvfjbBTOLH+6xTf9AYLGfyAhXOQmJqWOMt5K9kbsUg+q2qZThbvycJbipi6DKc6HAkA9Vm3pGG5Jmn+q9qa8p03uqAb6V1deIp9MSr9+5MyLWf3qb/fIR6QbPA4F5g9Wx2sJbgUAQys6lWBh8DF/WUtP
-----END RSA PRIVATE KEY-----
"""


class Account:
    '''
    账户信息可以从以下地址注册
    http://10.10.23.116:41008/v1/script/create_user_api?phone=16522223333
    账号密码  dssj dssj123456
    16522223333
    {"code":200,"data":{"appId":"483154f183994cfea2764507a5c857ee","appSecret":"MIICdQIBADANBgkqhkiG9w0BAQEFAASCAl8wggJbAgEAAoGBAItA9ivffijUqaG3vXFBmvBuQoUtGTHHWIbpVwDVCJYVWmNhkUBvbygLJtaV7C+oolKPZtq9ucYZrlb7r15P/RBVvMt8X7GiN8wHmOv+hLw8kD8GXH3nk1MyywrCIpRsDRf++p5QWbFiCW3yLRcYMz4Z6Y1+KHzb6X4q7jeXwI9pAgMBAAECgYAxFL1vaz9xLrt3N2a7E2+DzKj/fYzCwctPCdFThsKW+4G3Q31Jo70e9QdEXOU5SwujY83RzUs8KnMLT3xZFoJQBkwxLfWCbICsDS/r/84AdThu8fjlHgJCC7rj8hJKy2106c/gCisejhxekLxN/ivr0XtsCdNZNzKpw/Gy37wY3QJBAOsAAYryk4FAYmRK8f6kAZOK7V4urpT+UCO/Ncc0OMD+ccajkBEVBQtUCjjLkMKivjjftc0klWorasug0oZvTz8CQQCXspwPE3RDfPQS6HISpuhaFGaWdZ0m8fkpeq9dp0ZhoZ/sD1oeeQJIYSGR9gwkUFHNvaHFb7o+LQZ58KgRrB9XAkBFJddOX1pv6dYJ1NOoLfIYzARUdkAAr2Q9YIIef4tDnpsz6+T0Yc7+Klhnpd6Opvx6F7mTB3S/rM7b5BKOZCpZAkAur1gZx6nrLyRKQWEB3n35YvfjbBTOLH+6xTf9AYLGfyAhXOQmJqWOMt5K9kbsUg+q2qZThbvycJbipi6DKc6HAkA9Vm3pGG5Jmn+q9qa8p03uqAb6V1deIp9MSr9+5MyLWf3qb/fIR6QbPA4F5g9Wx2sJbgUAQys6lWBh8DF/WUtP","expireDate":"2020-07-31 11:09:13","encryptToken":"684d4a77970a453fae44b8e96a0fe1ad"},"msg":"HTTP_OK","subCode":"0","subMsg":"success"}
    '''

    app_id = "483154f183994cfea2764507a5c857ee"
    encrypt_token = "684d4a77970a453fae44b8e96a0fe1ad"
    private_key_pem = private_key_pem


class ApiConfig:
    host = "http://10.10.23.116:41008"
    headers = {"application": "json", "charset": "utf-8", "OPENAPI_APP_ID": Account.app_id}


class Address:
    valid_btc = "1Hm6q7BWkdn2tbEA84gY4rNBF2tDekcccP"
    valid_eth = "0x5D281db74F856237556e428ad27922caDbfB3A02"
    invalid_btc = "1AbaXRtPE5tzQMNWhC8Va2RLj4Xg42g1L62"
    none = None
    type_int = 123456789
    type_float = 123.456789


class Code:
    btc_code = "BTC"
    eth_code = "ETH"
    error_code = "AAACCCC"
    none_code = None
    int_code = 123321


class OrderNo:
    valid_order_no = "123321"  # 缺少有效的订单号
    error_order_no = "123321123"
    int_order_no = 999999999999999
    str_order_no = "ChinaOrderNo"
    none_order_no = None


class BusinessNo:
    valid_business_no = "123321"  # 缺少有效的订单号
    error_business_no = "123321123NNNN"
    int_business_no = 999999999999999
    str_business_no = "ChinaOrderNo"
    none_business_no = None


class RespMsg:
    success_0 = {"code": 200, "msg": "ok", "subCode": "0", "subMsg": "success"}
    success_1 = {"code": 200, "msg": "HTTP_OK", "subCode": "0", "subMsg": "success"}

    error_35002 = {"code": 400, "msg": "HTTP_BAD_REQUEST", "subCode": "35002", "subMsg": "平台尚未开通该币种支持"}
    error_35006 = {"code": 400, "msg": "HTTP_BAD_REQUEST", "subCode": "35006", "subMsg": "地址格式不合法"}

    error_400 = {"code": 400, "msg": "该币种不支持", "subCode": "4003", "subMsg": "请求参数不合法"}

    error_400_4003 = {"code": 400, "msg": "数量范围 [1-100]", "subCode": "4003", "subMsg": "请求参数不合法"}
    error_35009 = {"code": 400, "msg": "HTTP_BAD_REQUEST", "subCode": "35009", "subMsg": "数量范围 [1-100]"}

    error_35000 = {"code": 400, "msg": "HTTP_BAD_REQUEST", "subCode": "35000", "subMsg": "商户订单号，平台订单号不能同时为空"}
    error_35001 = {"code": 400, "msg": "HTTP_BAD_REQUEST", "subCode": "35001", "subMsg": "代付订单不存在"}
    error_35008 = {"code": 400, "msg": "HTTP_BAD_REQUEST", "subCode": "35008", "subMsg": "请输入正确的订单号"}
