# -*- coding: utf-8 -*-
import json

import requests

from common.utils.logger import Logger

log = Logger(__name__).log()


class RequestVerify:

    def __init__(self, key, dictionary):
        self.test_value = None
        self.list_dictionary(key, dictionary)

    def list_dictionary(self, key, dictionary):
        if isinstance(dictionary, dict):
            for _key, _value in dictionary.items():
                if key == _key:
                    self.test_value = _value
                else:
                    self.list_dictionary(key, _value)
        elif isinstance(dictionary, list):
            for i in dictionary:
                self.list_dictionary(key, i)
        else:
            pass

    def __call__(self):
        return self.test_value


def str_convert_dict(_str_dict):
    '''
    :param _str_dict:
    :return: 字符型dict转成dict,常用语SQL储存的str_dict
    '''
    if isinstance(_str_dict, str):
        if _str_dict.startswith('{') and _str_dict.endswith('}'):
            try:
                _str_dict = json.loads(_str_dict)
            except:
                _str_dict = eval(_str_dict)
    return _str_dict


class Api(object):

    def __init__(self, **DataAll):
        '''
        :param Data:
        '''
        self.url = str(DataAll.get('url'))
        self.headers = DataAll.get('headers')
        self.method = str(DataAll.get('method'))
        self.param_type = str(DataAll.get('param_type'))
        self.params = DataAll.get('params')
        self._json = DataAll.get('json')
        self.cookies = DataAll.get('cookies')
        self.check_point = DataAll.get('check_point')
        log.info('request params {}'.format(DataAll))

    def request(self):
        response_dict = dict()
        try:
            if self.method.upper() == 'GET':
                response = requests.get(url=self.url, headers=self.headers, params=self.params, cookies=self.cookies)
            elif self.method.upper() == 'POST':
                if self.param_type.upper() == 'DATA':
                    response = requests.post(url=self.url, headers=self.headers, data=self.params, cookies=self.cookies)
                elif self.param_type.upper() == 'JSON':
                    response = requests.post(url=self.url, headers=self.headers, json=self.params, cookies=self.cookies)
                else:
                    log.error('request param type({}) not supported !!!'.format(type(self.param_type)))
                    return None
            else:
                log.error('request method({}) not supported !!!'.format(self.method))
        except requests.RequestException as e:
            log.error('RequestException url: %s\n%s' % (self.url, e))
            return ()
        time_total = response.elapsed.total_seconds()
        response_dict['status_code'] = response.status_code
        try:
            response_dict['json'] = response.json()
        except Exception as e:
            log.error(e)
            response_dict['json'] = ''
        response_dict['time_total'] = time_total * 1000
        log.info('response result: {}'.format(response_dict))

        # 获取的case check_point 不为None 做断言
        # if self.check_point is not None:
        #     for key, value in self.check_point.items():
        #         test_result = RequestVerify(key, response_dict)()
        #         Asserts().assert_equal(test_result, value,
        #                                'Test result({}:{}) == Expected result({}:{})'.format(key, test_result, key,
        #                                                                                      value))
        return response_dict
