# tool：PyCharm
# -*- coding: utf-8 -*-
import logging
import os
import time
from logging.handlers import RotatingFileHandler

from TesterHomeServer.settings import BASE_DIR, LOG_LEVEL

day = time.strftime('%Y-%m-%d', time.localtime(time.time()))
now = time.strftime('%Y-%m-%d-%H-%M', time.localtime(time.time()))


class Logger(object):
    def __init__(self, logger):
        level_dict = {
            1: logging.NOTSET,
            2: logging.DEBUG,
            3: logging.INFO,
            4: logging.WARNING,
            5: logging.ERROR,
            6: logging.CRITICAL
        }
        log_level = LOG_LEVEL
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(level_dict[log_level])
        log_path = '{}/logs/{}/'.format(BASE_DIR, day)

        if os.path.exists(log_path):
            log_name = os.path.join(log_path + now + '.txt')
        else:
            os.makedirs(log_path)
            log_name = os.path.join(log_path + now + '.txt')

        # fh = logging.FileHandler(log_name, encoding='utf-8')
        fh = RotatingFileHandler(log_name, maxBytes=1024000 * 10, backupCount=300, encoding='utf-8')
        fh.setLevel(level_dict[log_level])
        ch = logging.StreamHandler()
        ch.setLevel(level_dict[log_level])
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def log(self):
        return self.logger


def dog_log(remark, remark2):
    return '''

 *      ┌─┐       ┌─┐ + +
 *   ┌──┘ ┴───────┘ ┴──┐++
 *   │                 │
 *   │       ───       │++ + + +
 *   ███████───███████ │+
 *   │                 │+
 *   │       ─┴─       │
 *   │                 │
 *   └───┐         ┌───┘
 *       │         │
 *       │         │   + +
 *       │         │
 *       │         └──────────────┐
 *       │                        │
 *       │                        ├─┐      {}
 *       │                        ┌─┘      {}
 *       │                        │
 *       └─┐  ┐  ┌───────┬──┐  ┌──┘  + + + +
 *         │ ─┤ ─┤       │ ─┤ ─┤

————————————————
    '''.format(remark, remark2)
