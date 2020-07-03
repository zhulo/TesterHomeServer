private_key_pem = b"""
-----BEGIN RSA PRIVATE KEY-----
MIICdQIBADANBgkqhkiG9w0BAQEFAASCAl8wggJbAgEAAoGBAIaXe6J+c1EbvVQkbx5kWY5+e9Nd8hgrndlb5OF/iA3zgIQnpXE5U1DvMaudISWJir86LqPriFl2+0sdpzDazGd/EFabelIl5bbdhlbaTw5f98jVpNTTvYpFfLzPs66FfmGTxStWM7Q7f2xDvGwujyggN1+MTkoLtlgyEwgLz7cfAgMBAAECgYAAuynsxAsUUbZBksEXxSvHXmCF0WjTQMlmuN0RbIPsr3nvPdfkOY9+TQ5UBFJ9xbV/PG2sbkcbVU4gJlUWKtoZY8QU8yz/1XCTrGy/+5CV8aW4STeAc1+FA48CcRKlyqTb1HGGiITjGfNyY/6M+FzqPIsjomkuvn584YoNJCqqAQJBAOQGmA7vlTSC4HMpKEEzrshReOLSqr93xt5IxwILOsz1EBZrTdrTaFL+iegfrC3xvfM2gDS44Vmm9KZQ0E2cPMECQQCXGnzs8B/c9LvOu89zThBS25Le1rfVA1Pi3xsjKrTzCPpC2SmssRvYSfyluNIKw9Ctc8z4EyPk8xL8tMjYOovfAkBYPHT60praBwrzhSmekXFA8sXkf8Cy9pZtzZu0nsPSK8Jd6ofl9YiZFQYoXJkz7ieixaQ2wpPxLTneYcc5QQwBAkBQ9j1XivXXoz358EGgS4SNkN7qDWxkcysAVYCp4BkiW34UUV12DVOZGVOIzDWm1PK77V820LKb2u4ifw9aZExLAkBNAvK+o4hHuPzKy2nqVprBH15FoARv07sZFBraR2eqr/2J4b+CNV/uf8Hw5U5Q392SUyWCUzwlyMPNOQE2f7yN
-----END RSA PRIVATE KEY-----
"""


class Account:
    '''
    账户信息可以从以下地址注册
    http://10.10.23.116:41008/v1/script/create_user_api?phone=12366666667
    账号密码  dssj dssj123456
    {"code":200,"data":{"appId":"d9bb351282f14cc0a72ba9e3604c8e2e","appSecret":"MIICdQIBADANBgkqhkiG9w0BAQEFAASCAl8wggJbAgEAAoGBAIaXe6J+c1EbvVQkbx5kWY5+e9Nd8hgrndlb5OF/iA3zgIQnpXE5U1DvMaudISWJir86LqPriFl2+0sdpzDazGd/EFabelIl5bbdhlbaTw5f98jVpNTTvYpFfLzPs66FfmGTxStWM7Q7f2xDvGwujyggN1+MTkoLtlgyEwgLz7cfAgMBAAECgYAAuynsxAsUUbZBksEXxSvHXmCF0WjTQMlmuN0RbIPsr3nvPdfkOY9+TQ5UBFJ9xbV/PG2sbkcbVU4gJlUWKtoZY8QU8yz/1XCTrGy/+5CV8aW4STeAc1+FA48CcRKlyqTb1HGGiITjGfNyY/6M+FzqPIsjomkuvn584YoNJCqqAQJBAOQGmA7vlTSC4HMpKEEzrshReOLSqr93xt5IxwILOsz1EBZrTdrTaFL+iegfrC3xvfM2gDS44Vmm9KZQ0E2cPMECQQCXGnzs8B/c9LvOu89zThBS25Le1rfVA1Pi3xsjKrTzCPpC2SmssRvYSfyluNIKw9Ctc8z4EyPk8xL8tMjYOovfAkBYPHT60praBwrzhSmekXFA8sXkf8Cy9pZtzZu0nsPSK8Jd6ofl9YiZFQYoXJkz7ieixaQ2wpPxLTneYcc5QQwBAkBQ9j1XivXXoz358EGgS4SNkN7qDWxkcysAVYCp4BkiW34UUV12DVOZGVOIzDWm1PK77V820LKb2u4ifw9aZExLAkBNAvK+o4hHuPzKy2nqVprBH15FoARv07sZFBraR2eqr/2J4b+CNV/uf8Hw5U5Q392SUyWCUzwlyMPNOQE2f7yN","expireDate":"2020-08-02 16:06:27","encryptToken":"dc8db706ed8343b5be75c9dc41721920"},"msg":"HTTP_OK","subCode":"0","subMsg":"success"}
    '''


    app_id = "d9bb351282f14cc0a72ba9e3604c8e2e"
    encrypt_token = "dc8db706ed8343b5be75c9dc41721920"
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
