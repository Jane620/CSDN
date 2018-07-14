# -*- coding: utf-8 -*-
# @Time    : 2018/7/13 下午1:34
# @Author  : Jane
# @Site    : 
# @File    : turtle_demo.py
# @Software: PyCharm
# @Describe: 

import turtle

def demo():
    t = turtle.Pen()
    turtle.bgcolor("black")
    sides=6
    colors=["red","yellow","green","blue","orange","purple"]
    for x in range(360):
        t.pencolor(colors[x%sides])
        t.forward(x*3/sides+x)
        t.left(360/sides+1)
        t.width(x*sides/200)

    print("####结束####")

def demo2():
    import turtle
    t = turtle.Pen()
    turtle.hideturtle()
    turtle.bgcolor("white")
    turtle.speed(50)
    # sides=eval(input("输入要绘制的边的数目，请输入2-6的数字！"))
    sides = 6
    colors = ["red", "yellow", "green", "blue", "orange", "purple"]
    for x in range(360):
        t.pencolor(colors[x % sides])
        t.forward(x * 3 / sides + x)
        t.left(360 / sides + 1)
        t.width(x * sides / 180)
        t.left(91)

    print("####结束####")


def demo3():
    import turtle
    t = turtle.Pen()
    turtle.hideturtle()
    turtle.bgcolor("white")

    my_name = "WangJF"
    colors = ["red", "yellow", "purple", "blue"]
    for x in range(5):
        t.pencolor(colors[x % 4])
        t.penup()
        t.forward(x * 4)
        t.pendown()
        t.write(my_name, font=("Arial", int((x + 4) / 4), "bold"))
        t.left(92)
    turtle.done()

if __name__ == '__main__':
    demo3()