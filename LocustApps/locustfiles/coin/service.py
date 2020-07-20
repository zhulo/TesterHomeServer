import copy
import threading

import requests

from LocustApps.locustfiles.coin import consts as c
from common.utils.logger2 import Logger

log = Logger(__name__).log()


def get_access_token_with_headers_list(host, api, headers, username, password: str):
    if isinstance(username, list):
        users_headers = []
        for user in username:
            params = {"loginName": user, "password": password, "validCodeType": "email", "deviceName": "web",
                      "resolution": "1920x1080", "softwareVersion": "1.0.0", "deviceVersion": ""}
            resp = requests.post(url=host + api, headers=headers, data=params)
            if str(resp.status_code) == "200" and resp.json():
                response = resp.json()
                access_token = response['data']['accessToken']
                headers = copy.deepcopy(headers)
                headers['Authorization'] = access_token
                headers['user'] = user
                log.info('获取到用户 {} 的 headers: {}'.format(user, headers))
                users_headers.append(headers)
            else:
                log.error('获取用户 {} accessToken异常，终止测试'.format(username))
                return False
        return users_headers
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

    def create_coin_orders(self, user_headers_list, orders_nums, currency_code, buy_price, sell_price):
        '''
        单个币对的单个盘口的总委托数（单个盘口包括 买入 和 卖出）
        :param orders_nums: 单个盘口的总订单数
        :param user_headers_list:
        :param currency_code:
        :param buy_price:
        :param sell_price:
        :return:
        '''
        log.info('用户开始委托买入和卖出，单个盘口进行委托操作, 委托数为 {}'.format(orders_nums))
        for user in user_headers_list:
            for i in range(int(orders_nums / len(user_headers_list))):
                if self.trade_coin(user, currency_code, 'B', 'LIMIT', buy_price, 1) is False: return False
                if self.trade_coin(user, currency_code, 'S', 'LIMIT', sell_price, 1) is False: return False
        log.info('用户委托单个盘口的订单数完成，包括买入和卖出')

    def create_coin_height(self, coin_height_nums, orders_nums, user_headers_list, currency_code, init_price):
        '''

        :param coin_height_nums: 盘口深度，比如200 则卖出深度200，买入也是200
        :param orders_nums: 单个盘口的深度，如 200 则单个盘口买入委托订单数200，卖出订单数200
        :param user_headers_list:
        :param currency_code:
        :param init_price:
        :return:
        '''
        log.info('用户开始委托盘口深度，买入价格每次 -1 ， 卖出价格每次 + 1')
        for num in range(1, coin_height_nums + 1):
            buy_price = init_price - num  # 买入价格
            sell_price = init_price + num  # 卖出价格
            if sell_price == 0:
                log.error('卖出价格递减等于0，跳出循序，终止创建盘口深度，当前币对 {}'.format(currency_code))
                break
            if self.create_coin_orders(user_headers_list, orders_nums, currency_code, buy_price,
                                       sell_price) is False: return False


def reset_coin_thread(headers_list, currency_code_list):
    tasks = []
    for currency_code in currency_code_list:
        t = threading.Thread(target=TradeCoinSetUpData().create_coin_height,
                             args=(c.CoinHeightNums, c.OrdersNums, headers_list, currency_code, c.InitPrice))
        tasks.append(t)
        t.start()
