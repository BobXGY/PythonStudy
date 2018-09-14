#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 科赫曲线

import turtle


def koch(size, n):
    if n == 0:
        turtle.fd(size)
    else:
        koch(size / 3.0, n - 1)

        turtle.left(60)
        koch(size / 3.0, n - 1)

        turtle.left(-120)
        koch(size / 3.0, n - 1)

        turtle.left(60)
        koch(size / 3.0, n - 1)


def kochSnow(size, n):
    for i in range(1, 4):
        koch(size, n)
        turtle.left(-120)


# turtle.hideturtle()
turtle.speed(10000000000)
turtle.Turtle().screen.delay(0)
turtle.setup(800, 600)
turtle.penup()
turtle.goto(-350, 60)
turtle.pendown()
kochSnow(500, 4)
turtle.hideturtle()
turtle.done()
