# -*- encoding: utf-8 -*-
"""
@File    : locust_file.py
@Time    : 2020/7/9 16:27
@Author  : tester
@Software: PyCharm
"""
import time
from IccBank.wallet.monitor import WalletService
from IccBank.wallet.service import WalletApi
from locust import TaskSet, task, HttpUser

private_key_pem = b"""
-----BEGIN RSA PRIVATE KEY-----
MIICdQIBADANBgkqhkiG9w0BAQEFAASCAl8wggJbAgEAAoGBAJqEI+YkurLWieUJGBWWgWrFmyqKVsjE1ZO9WQKX1+kp79uWXoCDi/NI8ryVYmzrMdy/ffSXJb1EnDPlRFMMRjLsQCT0G1cE6lwQOpk0QdyJXGIxgZ3lNRqp41JsZCkjXU4cZ6QtNwS47cfuJL5tqIQoU7gbvkeImo0PtQJIMRltAgMBAAECgYB9SRWenztulLwcpMINhwqKm41T8fWqNseCUm5gxuP/n8xnfUZE5+TLL+P5+xpifFXiyrYDY6brDz2kaop62CH2FhuVmu3IfIfwfbTb2Bbu2KTog4DaEy1LxTg+2x1A+GHFPkoJXVvPexkNLJQsAJ+IPuZjG2PatiCXIaBjv4+ktQJBANwywe1I0VwwN4myRbGWxV5xjIUv0JfuQEPCr5COC4bBCJI48XWuJAohHhUs+xxwrPkyM+qGlv5oQgaPXFYORssCQQCzo4SEDEhW+drPG3dTCcoacAoNamNSArk5B8DNjAfqTeu2HMJbjWICr1onC1Q9alf3AhikNTozlv99mWrEamGnAkA93NS2wTpwV+uCd980oVMZ0XTVBjXoOTs8zjlct0tttFWgHvdXRHFDl0JIWLbDqrQt3njPbriFCO1jwmsCkkg5AkBEoT4pbL/easqLwYSO9vh9rTxJ79FOLbgx76JbZRpJC8f35XjjnVpKiE+7BvsCE7TTq7taUPORbijiBVDjBXmVAkBPVLgxr6cG6aM7dNo/MiIWQ2VAKY30k3a5Wuq6fkckgkbeeAJOXUdXBBTD6L7OMolN52anbsH+jHVLeSseryVX
-----END RSA PRIVATE KEY-----
"""
app_id = "c22cc2585c8e4235994cc045ef9edeba"
encrypt_token = "0736760a6cb34e67bba8ccb16fdac1e8"
headers = {"application": "json", "charset": "utf-8", "OPENAPI_APP_ID": app_id}


class WalletHttpTest(TaskSet):

    @task
    def create_address(self):
        timestamp = int(time.time() * 1000)
        params = {"appId": app_id, "currencyCode": "ETH",
                  "address": "0x33A490b1c0eE7bD221BAD990d7a2704Ce4C956f2",
                  "timestamp": timestamp, "nonce": str(timestamp), "signType": "RSA", "memo": ""}
        encrypted_data = WalletService().aes_encrypt(params, encrypt_token, private_key_pem)
        params = {"algorithm": "AES", "encryptedData": encrypted_data}
        resp = self.client.post("/v1/agentPay/addAddress", headers=headers, json=params)
        print("===========================")
        print(resp.json())
        WalletService().aes_decrypt(resp.json()['encryptedData'],encrypt_token)


class WebsiteUser(HttpUser):
    tasks = [WalletHttpTest]
    min_wait = 100
    max_wait = 1000
    host = "http://api.iccbank.net"
