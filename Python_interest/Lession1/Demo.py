# -*- coding: utf-8 -*-
# @Time    : 2018/7/7 下午5:32
# @Author  : Jane
# @Site    : 
# @File    : Demo.py
# @Software: PyCharm
import math

def fun(n):
    # n送入的为匹配数字的前面部分
    head = n
    tail = 6
    while head > 0:
        tail *= 10
        # 按照 floor()将
        head  = math.floor(head / 10)
    # 原始数据
    m = 10 * n + 6
    # 新移位的数据
    result = tail + n
    if result == m * 4:
        print(m)

if __name__ == '__main__':
    for x in range(1,100000):fun(x)
