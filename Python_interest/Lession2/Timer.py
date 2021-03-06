# -*- coding: utf-8 -*-
# @Time    : 2018/7/11 下午4:14
# @Author  : Jane
# @Site    : 
# @File    : Timer.py
# @Software: PyCharm


import time

class Timer(object):

    def __init__(self,verbose=False):
        self.verbose = verbose

    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time.time()
        self.secs = self.end - self.start
        self.msecs = self.secs * 1000
        if not self.verbose:
            print('elasped time is :{} ms'.format(self.msecs))