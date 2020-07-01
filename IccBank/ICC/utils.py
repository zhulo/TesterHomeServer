# -*- encoding: utf-8 -*-
"""
@File    : utils.py
@Time    : 2020/6/29 19:08
@Author  : tester
@Software: PyCharm
"""
import base64
import datetime
import hmac


def iso_local_timestamp():
    now = datetime.datetime.now()
    t = now.isoformat("T", "milliseconds")
    return t + "Z"


def iso_server_timestamp(host, end_point):
    import requests
    response = requests.get(host + end_point)
    if response.status_code == 200:
        return response.json()['iso']
    else:
        return ""


def api_hash(timestamp, method, end_point, body):
    return str(timestamp) + str.upper(method) + end_point + body


def api_sign(message, secret_key):
    mac = hmac.new(bytes(secret_key, encoding='utf8'), bytes(message, encoding='utf-8'), digestmod='sha256')
    d = mac.digest()
    return base64.b64encode(d)


def header_with_sign(api_key, sign, timestamp, passphrase):
    header = dict()
    header['Content-Type'] = 'application/json'
    header['ICC-ACCESS-KEY'] = api_key
    header['ICC-ACCESS-SIGN'] = sign
    header['ICC-ACCESS-TIMESTAMP'] = str(timestamp)
    header['ICC-ACCESS-PASSPHRASE'] = passphrase
    return header
