import time

import requests

now = time.strftime('%Y-%m-%d-%H-%M', time.localtime(time.time()))
url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=266b3d70-71b2-4e91-b011-9a8e763c3623"
params = {
    "msgtype": "markdown",
    "markdown": {
        "content": "实时新增用户反馈 {} <font color=\"warning\">132例</font>，请相关同事注意。\n>类型:<font color=\"comment\">用户反馈</font>\n>普通用户反馈:<font color=\"comment\">117例</font>\n>VIP用户反馈:<font color=\"comment\">15例</font>".format(
            now)
    }
}

resp = requests.post(url, json=params)
print(resp.status_code)
print(resp.json())
