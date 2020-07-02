# -*- encoding: utf-8 -*-
"""
@File    : create_trade.py
@Time    : 2020/7/2 11:41
@Author  : tester
@Software: PyCharm
"""

'''
1.创建币种 - 后台
2.同步元数据币种参数 - 后台
3.修改节点清算IP - 数据库更新
4.开启 - 后台

1.创建金融工具 - 后台
2.同步元数据参数 - 后台
3.修改节点 - 数据库更新
3.开启

1.平台下单 生成资金详情 - 前端
2.充值 - 数据库更新
'''
import requests

url = "http://idc.icctoro.com:7050/login.jsp"
params = {"username": "dssjsystem", "password": "111111", "hash_location": ""}
resp = requests.post(url, data=params, allow_redirects=False)
print(resp.cookies)

url = "http://idc.icctoro.com:7050/ws/action/menu/tags"
cookie = resp.cookies
# resp = requests.get(url,headers=)