# -*- encoding: utf-8 -*-
"""
@File    : service.py
@Time    : 2020/7/13 17:48
@Author  : tester
@Software: PyCharm
"""

import requests

from IccBank.wallet.monitor import str_to_md5


def email_access_token(login_email, password):
    if len(password) != 32: password = str_to_md5(password)

    host = "http://test.mobile.icctoro.com:7007"
    headers = {"Accept": "application/json", "Content-Language": "zh-cn", "Source-Site": "pc.jys", "userId": "",
               "Content-Type": "application/x-www-form-urlencoded", "Authorization": ""}

    params = {"loginName": login_email, "password": password, "validCodeType": 'email', "deviceName": "web",
              "resolution": "1920x1080", "softwareVersion": "1.0.0", "deviceVersion": ""}
    resp = requests.post(url=host + "/api/user/login/email", headers=headers, data=params)
    if str(resp.status_code) == "200" and resp.json():
        return resp.json()
    else:
        return '请求异常'
