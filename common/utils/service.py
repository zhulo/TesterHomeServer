# -*- encoding: utf-8 -*-
"""
@File    : service.py
@Time    : 2020/6/28 10:58
@Author  : tester
@Software: PyCharm
"""
import time

import pymysql
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from common.utils import consts as c
from common.utils import utils as u
from common.utils.logger import Logger

log = Logger(__name__).log()


class HttpService:

    def __init__(self, host):
        self.host = host

    def _get(self, end_point, headers, params):
        url = self.host + end_point + u.parse_params_to_str(params)
        return requests.get(url, headers=headers)

    def _post(self, end_point, headers, params, param_type: str = c.Data):
        url = self.host + end_point
        if param_type.upper() == c.Data:
            print('url: {}'.format(url))
            print("header {}".format(headers))
            return requests.post(url, headers=headers, data=params)
        elif param_type.upper() == c.Json:
            return requests.post(url, headers=headers, json=params)
        else:
            log.error('参数类型不支持!')
            return None

    def request(self, method, end_point, headers, params, param_type=c.Data):
        response = None
        if method.upper() == c.Get:
            response = self._get(end_point, headers, params)
        if method.upper() == c.Post:
            print('===========')
            print(headers)
            response = self._post(end_point, headers, params, param_type)
            print(response.status_code)
            print(response.text)
        if response is not None and str(response.status_code) == c.ResponseStatus:
            response_time = response.elapsed.total_seconds()
            try:
                resp = response.json()
                resp[c.ResponseTime] = response_time
                return resp
            except Exception as e:
                log.error(e)
        else:
            log.error("http 接口请求异常!")


class HttpService2(object):

    def http(self, api_url, method, **data):

        headers = data.get(c.Headers)
        param_type = data.get(c.ParamType)
        params = data.get(c.Params)

        try:
            resp = None
            if method.upper() == c.Get:
                resp = self._get(api_url, headers, params)
            elif method.upper() == c.Post:
                resp = self._post(api_url, headers, param_type, params)

            resp_time = resp.elapsed.total_seconds()

            response = dict()
            response[c.Status] = resp.status_code
            response[c.RespTime] = resp_time
            response[c.Response] = resp.json()
            log.info(response)
            return response
        except Exception as e:
            log.error(e)

    def _post(self, api_url, headers, param_type, params):
        if param_type.upper() == c.Json:
            return requests.post(url=api_url, headers=headers, json=params)
        elif param_type.upper() == c.Data:
            return requests.post(url=api_url, headers=headers, data=params)

    def _get(self, api_url, headers, param):
        return requests.get(url=api_url, headers=headers, params=param)


class DataBaseService(object):
    def __init__(self, config):
        '''
        :param config: 数据库配置
        '''
        self.conn = pymysql.connect(**config, charset='utf8')
        self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    def query(self, sql, fetchone):
        '''
        :param sql: sql 语句
        :param fetchone: True查询一条,False查询所有
        :return:
        '''
        try:
            self.cursor.execute(sql)
            log.info("SQL: {}".format(sql))
            return self.cursor.fetchone() if fetchone else self.cursor.fetchall()
        except Exception as e:
            log.error(e)
            return None
        finally:
            self.cursor.close()
            self.conn.close()

    def modify(self, sql):
        '''
        :param sql:
        :return: 增删改
        '''
        try:
            self.cursor.execute(sql)
            log.info("SQL: {}".format(sql))
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            log.error(e)
        finally:
            self.cursor.close()
            self.conn.close()


class Dictionary:

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


class UiService:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, element, seconds):
        wait = WebDriverWait(self.driver, seconds, 0.5)
        return wait.until(expected_conditions.visibility_of_element_located((By.XPATH, element)))

    def click(self, element, seconds=10):
        self.find_element(element, seconds).click()

    def input(self, element, value, seconds=10):
        self.find_element(element, seconds).send_keys(value)

    def refresh(self):
        time.sleep(1)
        self.driver.refresh()
        time.sleep(2)
