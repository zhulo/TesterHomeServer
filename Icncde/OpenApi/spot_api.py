# -*- encoding: utf-8 -*-
"""
@File    : spot_api.py
@Time    : 2020/6/29 14:51
@Author  : tester
@Software: PyCharm
"""
from Icncde.OpenApi import consts as c
from Icncde.OpenApi.client import OpenApiRequest


class IccOpenApi(OpenApiRequest):
    def __init__(self, host, api_key, api_secret_key, passphrase, use_server_time=True):
        OpenApiRequest.__init__(self, host, api_key, api_secret_key, passphrase, use_server_time)

    def api_get_ticker(self, instrument_id):
        '''
        公共-获取某个ticker信息
        获取币对的最新成交价、买一价、卖一价和24小时交易量的快照信息
        :param instrument_id:
        :return:
        '''
        return self.http_request(c.GET, c.SPOT_SPECIFIC_TICKER + str(instrument_id) + '/ticker', {})

    def api_take_order(self, instrument_id, side, size, price, _type='LIMIT'):
        '''
        币币交易提供限价单和市价单和高级限价单下单模式。只有当您的账户有足够的资金才能下单。
        一旦下单，您的账户资金将在订单生命周期内被冻结。被冻结的资金以及数量取决于订单指定的类型和参数。
        :param instrument_id: 币对,如：BTC_USDT_ICNCDE_ENCRY
        :param side: 买卖类型：B-买 S-卖
        :param size: 买入或卖出的数量
        :param price: 限价单（价格）必填
        :param _type: LIMIT-限价 MARKET-市价
        :return:
        '''
        params = {'instrument_Id': instrument_id, 'side': side, 'type': 'LIMIT', 'size': size,
                  'price': price}
        # params = {'instrument_Id': instrument_id, 'side': side, 'type': _type, 'size': size,
        #           'price': price}
        return self.http_request(c.POST, c.SPOT_ORDER, params)



