import time

from IccBank.wallet.conf import Account, RespMsg, ApiConfig
from IccBank.wallet.request import Api
from IccBank.wallet.rule import WalletApiRequest

API = WalletApiRequest()


class WalletApi:

    def register_user(self):
        phone = "1" + str(int(time.time()))
        request_data = {"url": ApiConfig.host + "/v1/script/create_user_api", "method": "get", "param_type": "data",
                        "params": {"phone": phone}}
        resp = Api(**request_data).request()
        resp = resp['json']
        if str(resp['code']) == '200':
            data = dict()
            data['phone'] = phone
            data['appId'] = resp['data']['appId']
            data['appSecret'] = resp['data']['appSecret']
            data['encryptToken'] = resp['data']['encryptToken']
            print(data)
            return data
        else:
            return None

    def create_address(self, currencyCode, count):
        '''
        创建代收地址，分配给用户作为充币地址
        :return:
        '''
        timestamp = int(time.time() * 1000)
        params = {"appId": Account.app_id, "currencyCode": currencyCode, "count": count,
                  "batchNumber": "batchNumber" + str(timestamp), "timestamp": timestamp, "nonce": str(timestamp),
                  "signType": "RSA"}
        return API.request("/v1/address/agency/create", params, RespMsg.success_1)

    def check_address(self, currencyCode, address):
        timestamp = int(time.time() * 1000)
        params = {"appId": Account.app_id, "currencyCode": currencyCode, "address": address,
                  "timestamp": timestamp, "nonce": str(timestamp), "signType": "RSA"}
        return API.request("/v1/address/check", params, None)

    def add_address(self, currencyCode, address, memo=""):
        '''
        代收地址注册，绑定商户 -- 地址检测成功后，将地址注册到钱包服务，注册成功后才能调取代付接口
        :return:
        '''
        timestamp = int(time.time() * 1000)
        params = {"appId": Account.app_id, "currencyCode": currencyCode, "address": address,
                  "timestamp": timestamp, "nonce": str(timestamp), "signType": "RSA", "memo": memo}
        return API.request("/v1/agentPay/addAddress", params, None)

    def agentPay_proxyPay(self, currencyCode, address, amount, memo=""):
        '''代付接口'''
        timestamp = int(time.time() * 1000)
        params = {"appId": Account.app_id, "userBizId": "ID=" + str(timestamp), "subject": "test",
                  "currencyCode": currencyCode, "address": address, "memo": memo,
                  "amount": amount, "notifyUrl": "", "timestamp": timestamp, "nonce": str(timestamp),
                  "signType": "RSA"}
        return API.request("/v1/agentPay/proxyPay", params, None)

    def agentPay_query(self, userBizId):
        timestamp = int(time.time() * 1000)
        params = {"appId": Account.app_id, "userBizId": userBizId, "timestamp": timestamp, "nonce": str(timestamp),
                  "signType": "RSA"}
        return API.request("/v1/agentPay/query", params, None)


class WalletData(WalletApi):
    def eth_recharge_address(self):
        return self.create_address("ETH", 5)

    def bind_address(self):
        '''
        已有资金的地址。绑定在目前新账户的代付地址
        :return:
        '''


if __name__ == '__main__':
    api = WalletApi()
    # api.create_address("IONC", "10")
    # api.check_address("BTC", "15aNiDaxCcLJNijXmA1dUVLAW9xv4b8zwz")
    # api.add_address("XRP", "rUzWJkXyEtT8ekSSxkBYPqCvHpngcy6Fks", "1014926")
    # api.agentPay_proxyPay("BCH", "38ABWBSPtAY8mrq4T9uXQSDXBaAxaEfYYH", "0.009")
    api.agentPay_proxyPay("XRP", "rUzWJkXyEtT8ekSSxkBYPqCvHpngcy6Fks", "1", '1014926')
    # api.agentPay_proxyPay("USDT_OMNI", "3FvsWRb1BgfadARzcAzMhU87VWaGcDj72H", "1")

# '''
# {"code":200,"data":{"appId":"0984dc8154444bc198323c07bdee961e","appSecret":"MIICdgIBADANBgkqhkiG9w0BAQEFAASCAmAwggJcAgEAAoGBAKzJsQfZh6Au17DOV/KOs8kxZhniUf0+o1AOJqbpD2RH+qqh27WPrt6UcAl3hBLLMUbHZEwDf6y7jrr12A1QDlqVFYsaEALBtlQSqXkimpIlqnrPijc4plhv/BJUwlSqA/NHdvzTWGCbvwSI7y9RLH+ncCtuXphEDYdOUwK664kNAgMBAAECgYBxkynAZSYXDnNMjnWUxGQ8zTG1teP6uF+U0ZhqgitR2VZVLotCrq1dNOjn8B1qVRGQ2qN8q5gSrD5Hei2HoqWrpFcXGUaVqwplLR5HHR+/j9Z5Qe9emVuKGffDjFrT3iBzjys/rtN8Di6f8q+Nf/5TLqsOn7OIkbBXHzVZH+VRwQJBANggwdGlbyyiYBIEoodINYYLdyPtkkrarSnuCU1Tm0+VdQqQafB4zoXpzS54INJPJeqZSSF5ccj13Nm0N2gZsmkCQQDMqhPu2YVw3+TKxUKmEqntwXOm/yKyMHv/E28izWnw7EEsQZxq+mog5Od5wB18W509rQca4V6AXTnzbEqGlwUFAkAzn69sCh4CBU75Ps4rjh3qxLZSiJ6W7qDKESd7purEGaj5OwFzBQgfiHcQEHWWhn1CChcjvcRmAgQcpCVP4kNxAkAiYG74r5C6ZOEJLhkDzB6+0L+cTT6Gr54kOh9wuRASZ5yK0npzfZxV6hz3Vk2dlcXTljybRz+YUBBr0sSx1qwBAkEA0hn4yRvTltoQzK3pm8Qz+YvpzFnCRbQ6VoKqoBmoDHMFJjKHG1LK+wnwOSMOsqGcunu56vHlh7ptPB6u99cnCw==","expireDate":"2020-07-23 10:06:06","encryptToken":"e0163c4c65704ac0b6ab1324e3e76ed4"},"msg":"HTTP_OK","subCode":"0","subMsg":"success"}
# '''
# if __name__ == '__main__':
#     api = WalletApi()
#     # 1. 注册商户
#     # api.register_user()
#     # {'phone': '11592232990', 'appId': '0c682d96bb9c4e5585d632d5d280a1d2', 'appSecret': 'MIICdgIBADANBgkqhkiG9w0BAQEFAASCAmAwggJcAgEAAoGBAIdSb86oihQENqgxmDsxXILxus+FaFomh9cvi+JEgeROlJY50o2lw934MmLQ5+9uanI6VeHCYAk1pAsM1zxytoWx2Tsuq6tXqUBj941PI0i31CSYueqOAOCGngfltyM8ZLwPjX9P5hrr89l1AkLi4tQC0zizMvyvx3DnrtqM4+F5AgMBAAECgYBYqDjaY297Z7tLfJqpBVD/9VGYDmZs0dujruHtz0ZuhtEwjxeUd+sYbTjNpuKd6nBRAEkuDMQQpJUiLDqDvwA3JphfAO+jaA0fN9l1HlfYKFKSesMA/xz18cUzsGnJHECv9nAknc28z4stXpzwmD5ClJpF7ikCo1oQKiEd2BOj1QJBANlXgHg2cc4eiZO8rYStyx9fHl+nEWyuXDGlX/58HSAq7TL+yGwQuvl/RL2sbToEs1x8c0vA0+DtYra1mLe6Me8CQQCfZDmFfICpmProevNM6aG5wfxiHuMobfd2zNMnz399LcHSSLARy06Qxr8xOaNU18puTQaRkD1yc3Xa94c83esXAkEAs76iCMk+JXEr5nrMJkZ1DmTkAcdxqagppwVV9mk+zTOzJ9F+f6D2gRC4EQVg7/KjQ4HI+IVotUSdtu1Id+oNEQJAT2cWYLFNRy+2junxGneo4WkJ2beZYiKmDMCs0EBGOo346FDdpX+qe+UGifc0rqdxaNFmXE2GzuVF6Pc2n9PNsQJAHx7A6tINs136RNigPutIodsTzl5cbA9RSKfGASCMzdTpo6cXrDzUeyRsGM9cxAd5knxEcejVKJknHY9N2PeZBw==', 'encryptToken': 'ee52b187966144e7b2b00759e1939898'}
#
#     # 2.商户绑定充值地址
#     # api.add_address("FIL", "t1dgixrchyspmpw4qsk6rucgarotlvaobynlknfyy")
#     api.create_address("FIL", 3)
#     # api.agentPay_proxyPay("FIL", "t1zgojev32amgzkglvcjrnybqhdjiptkdtpkzx27y", 20)
#     # api.check_address("FIL","t1d6fapnsdpwdrrwqv5tmfd3u3mp5aibqimybndoy")
#     # api.agentPay_query("ID=1592891232660",'')
#
#     # 代付订单查询
#     '''
#     businessNo > mchOrderNo
#     :param mchOrderNo: 商户订单号  == user_biz_id
#     :param businessNo: 平台订单号  == ID
#     mchOrderNo='ID=1592553520728'
#     businessNo='1041155454606622720'
#     '''
#     # api.agentPay_query(mchOrderNo='ID=1592553520728', businessNo='1041155454606622720')
#     '''
# // 核对信息，获取userid
# select id from didipay_user.user_info where phone = "11592232990";
#
# // 核实加密信息
# select * from didipay_user.user_api where user_id = "1039811031565713408";
#
#
# // 获取商户开通的钱包信息 - 默认开通
# select * from didipay_account.account_info where user_id = "1039811031565713408";
#
#
# // 查看商户账户地址簿记录表, account_type_id 1 == 啥
# // 手动调用api add address 接口 添加了一条数据
# select * from didipay_account.account_address_book where user_id = "1039811031565713408";
#
# // 上面add的地址(商户自己添加的address)为啥没加入到active_address表里
# // 手动调用 create address 接口添加了N条数据
# select * from didipay_wallet.active_address where user_id = "1039811031565713408";
#
# //
#     '''
