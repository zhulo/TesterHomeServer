# -*- encoding: utf-8 -*-
"""
@File    : open_api_task.py
@Time    : 2020/6/29 15:35
@Author  : tester
@Software: PyCharm
"""
from Apps.ICC.openApi import consts as c
from Apps.ICC.openApi.spot_api import IccOpenApi
from common.utils.logger import Logger

log = Logger(__name__).log()

import random


class BusinessProcess(IccOpenApi):

    def __init__(self, host, api_key, api_secret_key, passphrase, use_server_time=True):
        IccOpenApi.__init__(self, host, api_key, api_secret_key, passphrase, use_server_time)

    def get_latest_ticker_info(self, instrument_id):
        '''
        获取到最新的盘口信息，获取不到取固定的配置盘口信息
        :param instrument_id:
        :return:
        '''
        latest_ticker_info = self.api_get_ticker(instrument_id)
        log.info('获取到币对 {} 最新信息'.format(instrument_id))
        best_ask = float(latest_ticker_info.get('bestAsk'))  # 买1
        best_bid = float(latest_ticker_info.get('bestBid'))  # 卖1
        if best_ask > 0 and best_bid > 0:
            log.info('获取到币对 {} 最新的盘口信息：best_ask: {}, best_bid: {}'.format(instrument_id, best_ask, best_bid))
            return [best_ask, best_bid]
        else:
            log.info('未获取到币对 {} 最新的盘口信息，设置固定的：best_ask: {}, best_bid: {}'.format(
                instrument_id, c.ConstsAsk, c.ConstsBid))
            return [c.ConstsAsk, c.ConstsBid]

    def taker_order_with_buy(self, instrument_id, setup=False):
        '''
        推送一条买入的订单，价格偏高，可以取best_ask值，amount 设置较大
        在推送多条卖出的订单，价格低于买入的价格， amount非常小
        :param instrument_id:
        :param setup: 默认为True，给卖出生成一条数据, 取买1的价格，amount较大
        :return:
        '''
        latest_ticker_info = self.get_latest_ticker_info(instrument_id)
        if setup:
            price = latest_ticker_info[0]
            size = format(5000, '.6f')
        else:
            price = float(format((latest_ticker_info[0] + latest_ticker_info[1]) / 2, '.3f'))
            size = format(random.uniform(1, 2), '.6f')
        log.info("根据获取到的币对信息，生成下单的信息")
        log.info("下单(买入)信息: 随机买入数量(size): {}".format(size))
        log.info("下单(买入)信息: 限价单(type='LIMIT')价格(price): {}".format(price))

        self.api_take_order(instrument_id, 'S', size, price, _type='LIMIT')

    # def taker_order_with_buy(self, instrument_id):
    #     latest_ticker_info = self.api_get_ticker(instrument_id)
    #     log.info('获取到币对 {} 最新信息'.format(instrument_id))
    #     best_ask = float(latest_ticker_info.get('bestAsk'))  # 买1
    #     best_bid = float(latest_ticker_info.get('bestBid'))  # 卖1
    #
    #     log.info('获取到币对 {} 最新的盘口信息：best_ask: {}, best_bid: {}'.format(instrument_id, best_ask, best_bid))
    #     if best_ask > 0 and best_bid > 0:
    #         price = float(format((best_ask + best_bid) / 2, '.3f'))
    #         size = self.random_amount()
    #
    #         log.info("根据获取到的币对信息，生成下单的信息")
    #         log.info("下单(买入)信息: 随机买入数量(size): {}".format(size))
    #         log.info("下单(买入)信息: 限价单(type='LIMIT')价格(price): {}".format(price))
    #
    #         self.api_take_order(instrument_id, 'B', size, price, _type='LIMIT')


if __name__ == '__main__':
    ic_api_key = '71f9deb815334b889a2ea5a8cd0f7ea9'
    ic_secret_key = '5888d82d5ab94b08b7b217f1f38db498'
    ic_passphrase = 'a111111'
    # ic_api_key = '71f9deb815334b889a2ea5a8cd0f7ea9'
    # ic_secret_key = '5888d82d5ab94b08b7b217f1f38db498'
    # ic_passphrase = 'a111111'
    ic_host = c.API_URL
    # end = '/openapi/spot/v1/instruments/EOS_USDT_ICNCDE_ENCRY/ticker' #  公共-获取全部ticker信息

    # BusinessProcess(ic_host, ic_api_key, ic_secret_key, ic_passphrase).get_latest_ticker_info("BTC_USDT_ICNCDE_ENCRY")
    BusinessProcess(ic_host, ic_api_key, ic_secret_key, ic_passphrase).taker_order_with_buy("BTC_USDT_ICNCDE_ENCRY")
