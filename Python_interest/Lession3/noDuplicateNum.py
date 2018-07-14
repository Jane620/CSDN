# -*- coding: utf-8 -*-
# @Time    : 2018/7/14 下午7:27
# @Author  : Jane
# @Site    : 
# @File    : noDuplicateNum.py
# @Software: PyCharm
# @Describe:  a = 1 -9 ,b = 0-9 , c = 0-9

def noDuplicateNum():

    count = 0
    l = range(10)
    for a in l[1:]:
        for b in l:
            if a == b:
                continue
            else:
                for c in l:
                    if c != b and c != a:
                        count += 1
                        print(a * 100 + b * 10 + c)
    print('总计:',count)

# 输入x，作为多少位数
def noDuplicateNum2(x):

    count = 0
    l = range(10)
    # 10 ** (x-1) 为最大位
    if not isinstance(x,int) or x <= 0:
        print('输入错误！')

    # 如何区分到底多少位数，以确定循环次数
    print('总计:', count)

if __name__ == '__main__':
    noDuplicateNum2()
