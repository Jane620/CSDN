# -*- coding: utf-8 -*-
# @Time    : 2018/7/12 下午1:53
# @Author  : Jane
# @Site    : 
# @File    : BackPutStr.py
# @Software: PyCharm
# @Describe: String back output


def BackOutputStr(message):

    result = ''
    if str is None:
        print("输入错误，入参不能为空")
    if not isinstance(message,str):
        result = str(message)

    print(result[::-1])

if __name__ == '__main__':
    message = "this is my word."
    import os
    env = os.environ or message
    print("env:",env)
    BackOutputStr(env)