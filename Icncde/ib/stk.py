# -*- encoding: utf-8 -*-
"""
@File    : stk.py
@Time    : 2020/7/15 16:56
@Author  : tester
@Software: PyCharm
"""
import datetime
import random
import time

from locust import TaskSet, task, HttpUser


class StkClientDemo(TaskSet):

    def on_start(self):
        pass

    @task(1)
    def ticker_mock(self):
        '''

        测试日志： 5个slave节点， 总用户 500 并发， 50 用户递增， 2020.6.8 14:45 开始
        :return:
        '''
        # url = "http://10.10.23.182:5181/quote/ib/ticker/mock"
        random_num = random.randint(50, 60)
        timestamp = round(time.time() * 1000)
        # codes从 icc_quote.quote_listing 取
        # stk_codes = ["USO", "XLU", "XLE", "IWM", "XLP", "XLK", "XLI", "XLV", "GLD", "EWJ", "RSX", "VGK", "EWA", "EEM"]
        # stk_codes = ["2318", "3968", "700", "939", "3690", "1093", "2628", "1876", "1299"]
        stk_codes = ['2318', '3968', 'IAU', 'QQQ', 'XOP', 'EFA', 'USO', 'XLU', 'XLE', 'IWM', 'XLP', 'XLK', 'XLI', 'XLV',
                     'GLD', 'EWJ', 'RSX', 'VGK', 'EWA', 'EEM', 'EWZ', 'VWO', 'DIA', 'MSFT', 'AAPL', 'FB', 'BABA', 'JPM',
                     'JNJ', 'V', 'WMT', 'PG', 'XOM', 'T', 'MA', 'BAC', 'HD', 'TSM', 'VZ', 'DIS', 'RDS B', 'KO', 'RDS A',
                     'INTC', 'MRK', 'CVX', 'WFC', 'BA', 'UNH', 'HDB', 'CMCSA', 'CSCO', 'NVS', 'PFE', 'PEP', 'TM', 'BUD',
                     'ORCL', 'CHL', 'MCD', 'C', 'HSBC', 'NKE', 'MDT', 'ABT', 'SAP', 'ADBE', 'COST', 'CRM', 'TOT', 'PDD',
                     'RY', 'TD', 'SU', 'ACN', 'BHP', 'PKX', 'AVGO', 'PBR', 'ABEV', '1321', '700', '939', '3690', '1093',
                     '2628', '1876', '1299', '1398', '941', '16', '1211', '285', '175', '5', '1810', '2382', '2269',
                     '288', '883', '8411', '4689', '3250', '8306', '7647', '8604', '8918', '5020', '9437', '9984',
                     '8002', '9434', '8031', '3402', '6584', '9433', '4005', '7201', 'LLOY', 'VOD', 'BP.', 'BARC',
                     'GLEN', 'BT.A', 'CNA', 'HSBA', 'RBS', 'LGEN', 'TSCO', 'MRW', 'ALSPW', 'ALCYB', 'UG', 'ALEUP',
                     'ALIMP', 'ORA', 'ACA', 'CS', 'SAFOR', 'VK', 'ENGI', 'FP', 'BNP', 'WLN', 'RNO', 'CGG', 'ALTBG',
                     'STM', 'J36', 'U11', 'F34', 'DBK', 'SHF', 'BAS', 'FRE', 'ABR', 'LHA', 'SPY', 'GDX', 'XLF']
        random_code = random.randint(0, len(stk_codes) - 1)
        random_volume = random.randint(50, 100)
        end_point = '/quote/ib/mock/ticker'
        params = {"code": stk_codes[random_code], "bid": random_num, "ask": random_num, "price": random_num,
                  "timestamp": timestamp, "volume": random_volume,
                  "bidCanAutoExecute": "true", "askCanAutoExecute": "true"}
        # r = self.client.get(end_point, params=params)
        r = self.client.get(end_point, params=params, name='mock')
        print(params)
        print(str(timestamp) + ' ' + str(datetime.datetime.now()) + ' ' + str(r.text))


class WebsiteUser(HttpUser):
    tasks = [StkClientDemo]
    min_wait = 100
    max_wait = 1000
    host = "http://10.10.23.182:5181"


'''
log
linux ssh work1
/data/icc-quote-ib/logs

SQL: DBeaver
SELECT   t.*,DATEADD('MILLISECOND',TIMESTAMP ,TIMESTAMP '1970-01-01 08:00:00' ) AS GMT8       
FROM PUBLIC.KLINE_M1_02318_HKD_SEHK t ORDER BY t."TIMESTAMP"  DESC;
'''

# locust -f locusts\stk.py --host=http://10.10.23.182:5181

# master: locust -f locusts\stk.py --master --host=http://10.10.23.182:5181
# salve: locust -f locusts\stk.py --salve --host=http://10.10.23.182:5181
# salve2:  locust -f locusts\stk.py --worker --master-host=192.168.21.14 --host=http://10.10.23.182:5181


'''
节点信息:
ssh master:
# jps
112229 icc-quote-coinbase.jar
4312 CommandLineStartup
26091 icc-quote-web.jar

ssh work1:
# jps
114391 icc-quote-websocket.jar
7036 icc-quote-ib.jar
ssh work2:
# jps
114391 icc-quote-websocket.jar
7036 icc-quote-ib.jar
'''
