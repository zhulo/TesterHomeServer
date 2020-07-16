import copy

import requests

from LocustApps.locustfiles.coin import consts as c
from common.utils.logger2 import Logger

log = Logger(__name__).log()


def user_with_currency_code(user_list, currency_code_list):
    log.info("一共启动 {} 个用户， {} 币对进行压测".format(len(user_list), len(currency_code_list)))
    user_with_code_list = []
    for username in user_list:
        for currency_code in currency_code_list:
            user_with_code_dict = {}
            user_with_code_dict[username] = currency_code
            user_with_code_list.append(user_with_code_dict)
    log.info(user_with_code_list)
    log.info('所有用户与币对遍历组合共获得 {} 排列组合，启动对应线程进行初始化盘口数据......'.format(len(user_with_code_list)))
    return user_with_code_list


def get_access_token_with_headers_list(host, api, headers, username, password: str):
    if isinstance(username, list):
        user_with_headers_dict = []
        for user in username:
            user_headers = {}
            params = {"loginName": user, "password": password, "validCodeType": "email", "deviceName": "web",
                      "resolution": "1920x1080", "softwareVersion": "1.0.0", "deviceVersion": ""}
            resp = requests.post(url=host + api, headers=headers, data=params)
            if str(resp.status_code) == "200" and resp.json():
                response = resp.json()
                access_token = response['data']['accessToken']
                headers = copy.deepcopy(headers)
                headers['Authorization'] = access_token
                user_headers[user] = headers
                log.info('获取到用户 {} 的 headers: {}'.format(user, headers))
                user_with_headers_dict.append(user_headers)
            else:
                log.error('获取用户 {} accessToken异常，终止测试'.format(username))
                return False
        return user_with_headers_dict
    else:
        params = {"loginName": username, "password": password, "validCodeType": "email", "deviceName": "web",
                  "resolution": "1920x1080", "softwareVersion": "1.0.0", "deviceVersion": ""}
        resp = requests.post(url=host + api, headers=headers, data=params)
        if str(resp.status_code) == "200" and resp.json():
            response = resp.json()
            access_token = response['data']['accessToken']
            headers['Authorization'] = access_token
            log.info('获取到用户 {} 的 headers: {}'.format(username, headers))
            return headers
        else:
            log.error('获取用户 {} accessToken异常，终止测试'.format(username))
            return False


class TradeCoinSetUpData:

    def trade_coin(self, headers, currency_code, side, operate_type, price, amount):
        '''
        :param headers: 带有 access_token 的headers
        :param currency_code:
        :param side: B 买入 、S 卖出
        :param operate_type: "LIMIT" == 限价买入
        :param price: 价格
        :param amount: 数量
        :return:
        '''
        side_text = "委托买入" if side == 'B' else "委托卖出"
        operate_type_text = "市价" if operate_type == 'MARKET' else "限价"
        params = {"code": currency_code, "source": "PC", "side": side, "type": operate_type, "price": price,
                  "qty": amount, "accountType": "1004", "autoBorrow": "false"}
        resp = requests.post(url=c.HOST + c.CoinEntrustAPI, headers=headers, data=params)
        if str(resp.status_code) == '200' and resp.json():
            log.debug('Pass! {}-{}-{}-{}-{}-{},resp:{} '.format(headers['user'], currency_code, side_text,
                                                                operate_type_text, amount, price, resp))
        else:
            log.error("委托失败,终止测试,接口返回状态: {}, 参数: {}".format(resp.status_code, params))
            return False

    def set_coin_trade_entrust_amount(self, headers, currency_code, best_ask, best_bid, amount):
        if self.trade_coin(headers, currency_code, 'B', 'LIMIT', best_ask, amount) is False:
            return False
        # 卖出
        if self.trade_coin(headers, currency_code, 'S', 'LIMIT', best_bid, amount) is False:
            return False


def setup_coin_data(user_list, currency_code_list):
    tasks = []
    headers_list = get_access_token_with_headers_list(c.HOST, c.EmailLoginAPI, c.Headers, c.UsernameList,
                                                      c.Password)
    for i in user_with_currency_code(user_list, currency_code_list):
        t = threading.Thread(target=TradeCoinSetUpData(c.HOST).one_headers_trade_coin,
                             args=(headers_list[i], 500, 20, len(headers_list), 50, 1))
        tasks.append(t)
        t.start()

if __name__ == '__main__':
    user_with_headers_list = get_access_token_with_headers_list(c.HOST, c.EmailLoginAPI, c.Headers, c.UsernameList,
                                                      c.Password)
    user_with_currency_code_list = user_with_currency_code(c.UsernameList, c.CurrencyCodeList)
    from pprint import pprint
    pprint(user_with_headers_list)
    for user,headers in user_with_headers_list.items():
        for user_with_currency_dict in user_with_currency_code_list:
            if user == user_with_currency_dict.keys():
                TradeCoinSetUpData().trade_coin(headers,)


