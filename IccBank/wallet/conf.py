private_key_pem = b"""
-----BEGIN RSA PRIVATE KEY-----
MIICdgIBADANBgkqhkiG9w0BAQEFAASCAmAwggJcAgEAAoGBAI5BR2omOyPsT9PQSdbzoNRnwGfNjqCsF3Dt9ueI69mDiUFjaT/TwIYJ2VBjkrlSB5j1KdD92nx7Za+F0TmocaxT/rEWNqHsozxPEZMzekk/SjM3tV+Dw6V8pnp0HGcP32bLzTHJiavGHdWVlLewSVI+IhLPnIemRfK9AehNbC6JAgMBAAECgYAbgy6PrhM0EGkj+x28z+OkEOjaapwSIRZrheqBvy52JAVwuwxJBuguREteS9O9ucq0X34V6HLQLoFtIAFmGFjbhJXvhgUovXyiH4pifQhpZdoilJoyFlc8uic4ZK1fZG+0O41VzvkOwGeaaqi0dFJkBzyGJd0ZnEgcf3cyQKa6PQJBAL/1SObxx/IvC9eEe0Jl1anQbM6bg8Cm/hzaUjszyZFc8aDh3nuatr0/RMvfvrHf3gM3TRo/q3xuLEoNblnZDF8CQQC9tvWqzTpjDD30iqYpiH8CnF06h9vfXH7zn0SPo+xJl0R8tOL2DtV/Vtf/gomvr6w5c6QnK05+B9QxE+iyLS4XAkAoK9nE0uZoDWZqBMSSwaL0NbT/i9YHtCrLuPiqgQz2yb+bTolzzo3djucDz2Al81aPz7vn+VkW4iuMl8D3No/7AkEAmb9EqP9Zahvpud0DfHVaOUtvYpfn4MSdPeK9NYurWph0sHwH01GCRIik1DV+UBsWgBjv166JFipSFNQFqSBkUQJAYG760IuctcnGe7lz+qRHpU20pv2gD/+dy2HX8imydgjZWMNAN+DClNTALjUdIH7FJ3uHpcoc3Mu5NRaFH34gUw==
-----END RSA PRIVATE KEY-----
"""


class Account:
    '''
    账户信息可以从以下地址注册
    http://10.10.23.116:41008/v1/script/create_user_api?phone=12366667777
    账号密码  dssj dssj123456
    {"code":200,"data":{"appId":"d4f998ab4baa410786286a15a25c25d6","appSecret":"MIICdQIBADANBgkqhkiG9w0BAQEFAASCAl8wggJbAgEAAoGBAKAMJbl4Wu4/eUmnHA6eW2HKkjj5R9Ik/dTOKJ83UeXJ0ZMbkK4/O/BBP183U9sZukIAEpBT6h2Sey0mt9DbzNQaYy45Q7COENJShn7BKv5DmRm8q1kMDF8lXmw9L0QSZPGIyT//Xizi7e/NE4kCQqU27MhhlpaphdJvKuWtMk3TAgMBAAECgYBwwj4t3tLJumScdKT606z0SAEfLNnh/3fqX1kVW6dSqw8BgtE7QofbLE0Wq2dkHUsxxtVNZCG0tggcdoPZHZK/1bqyL7dIms7IHaPWvLokKAuNNoiQlLgiL+P93YV5n+3k4ZUWlfW6eEpG2X8p9D6DLUCy5gZ4uLF1PHKEqeO06QJBAPgDiG8gSgcxh9qpgTZKjADQvMMgj1+PIisgNqISrgL3VJE0qV9sJVALKVZbNzCu57BZ5jdHMTJSQwrvJDs2nZ0CQQClM3njFGxjAOr7FmlLSgGTfl3chMQWyvzDNWluieMRu1RfQTM/T5l2arvA17FS2j1617MEfANlXqa9SGhDCXYvAkACjubFXqvkzxn7o2v1x2cSSxTnXlqcPbm4gCiQG2k4Fp0Esmpc1Zy86qCOh3pWQjeZlhPN1ionvrl6T2UsRy/xAkB0ZbCbrugvWZY3E7NcuOgjZAX+Og1vgdZWNGv01nKHK9Zmxym0kgEuzkU7ur3WAq8OvqwDnN1Hr0kMVNghY6lBAkAzhMdU+H1xd+YPIl1nUEXDaXcCKK3q8vF/mIDgGUnn/Kqh7u4soRT80LhDa0YtM7hsKHAL3Wf84ieX2XFXhNxz","expireDate":"2020-08-02 20:11:02","encryptToken":"bd42b0d753b745b0b66465a8de2b93cd"},"msg":"HTTP_OK","subCode":"0","subMsg":"success"}
    '''

    app_id = "2de1498a7cbd4380a669464dbeb6abc9"
    encrypt_token = "b2f7e45faf0347eea2efd26ba26c086c"
    private_key_pem = private_key_pem


class ApiConfig:
    host = "http://10.10.23.116:41008"
    # host = "http://58.33.9.130:41008"
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
