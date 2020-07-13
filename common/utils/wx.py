import time

import requests

# now = time.strftime('%Y-%m-%d-%H-%M', time.localtime(time.time()))
# url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=266b3d70-71b2-4e91-b011-9a8e763c3623"
# params = {
#     "msgtype": "markdown",
#     "markdown": {
#         "content": "实时新增用户反馈 {} <font color=\"warning\">132例</font>，请相关同事注意。\n>类型:<font color=\"comment\">用户反馈</font>\n>普通用户反馈:<font color=\"comment\">117例</font>\n>VIP用户反馈:<font color=\"comment\">15例</font>".format(
#             now)
#     }
# }
#
# resp = requests.post(url, json=params)
# print(resp.status_code)
# print(resp.json())

import yaml
from TesterHomeServer.settings import BASE_DIR

WxWebHookPath = BASE_DIR + r'\common\resources\WxWebHook.yaml'


def web_hook_push_msg(hook_tag):
    now = time.strftime('%Y-%m-%d-%H-%M', time.localtime(time.time()))
    with open(WxWebHookPath, encoding='utf-8') as file:
        content = yaml.unsafe_load(file)
    headers = content['headers']
    url = content[hook_tag]
    params = {
        "msgtype": "markdown",
        "markdown": {
            "content": "实时新增用户反馈 {} <font color=\"warning\">132例</font>，请相关同事注意。\n>类型:<font color=\"comment\">用户反馈</font>\n>普通用户反馈:<font color=\"comment\">117例</font>\n>VIP用户反馈:<font color=\"comment\">15例</font>".format(
                now)
        }
    }
    resp = requests.post(url, headers=headers, json=params)
    print(resp.status_code)


if __name__ == '__main__':
    web_hook_push_msg('trade_coin')
