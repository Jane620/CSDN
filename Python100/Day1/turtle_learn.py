# -*- coding: utf-8 -*-
# @Time    : 2018/7/13 下午1:43
# @Author  : Jane
# @Site    : 
# @File    : turtle_learn.py
# @Software: PyCharm
# @Describe: 

import turtle as t

def demo(x,y):
    init()
    #t.colormode(111)
    '''
    t.setx(-100)
    t.sety(100)
    t.fd(100)
    t.seth(80)
    #t.right(90)  # x轴向上偏角度
    #t.left(90)   # x轴向下偏角度
    t.bk(20)
    '''
    t.goto(x,y)
    t.color('red','pink')
    t.begin_fill()
    t.circle(30)
    t.end_fill()


def init():
    t.pensize(4) #画笔大小
    t.pencolor('red')
    t.shape("turtle")
    #turtle.shape('turtle') #画笔样子
    #t.hideturtle()  #隐藏默认画笔
    t.setup(800,600) #画板大小
    t.speed(1) #画笔画画速度


if __name__ == '__main__':
    demo(-10,100)
    t.done()