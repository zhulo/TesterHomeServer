# -*- encoding: utf-8 -*-
"""
@File    : utils.py
@Time    : 2020/6/29 11:13
@Author  : tester
@Software: PyCharm
"""

from common.utils.logger import Logger

log = Logger(__name__).log()


def parse_params_to_str(params: dict):
    '''
    request get 参数转换
    :param params:
    :return:
    '''
    if isinstance(params, dict):
        url = '?'
        for key, value in params.items():
            url = url + str(key) + '=' + str(value) + '&'
        return url[0:-1]
    else:
        log.error('格式不支持！')
        return ""
