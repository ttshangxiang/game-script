#coding=utf-8
#pylint: disable=maybe-no-member
'''
安卓模拟器的一些操作
'''

import mouse
import win
import time
import random
import math

sleep = time.sleep

#找窗口
hwnd = win.getWindow('Bluestacks App Player')
#置顶
win.foucs(hwnd)
#睡一秒
sleep(1)
#窗口四个角位置
(left, top, right, bottom) = win.getWindowRect(hwnd)
#宽高
w = right - left
h = bottom - top

#随机数
def rd():
    return random.random()

#拖动
def drag(x0, y0, x, y, delay):
    x0 = int(x0)
    y0 = int(y0)
    x = int(x)
    y = int(y)
    mouse.move(x0, y0)
    sleep(0.2)
    mouse.down()
    for index in range(20):
        mouse.move(x0 - (x0 - x) / 20 * index, y0 - (y0 - y) / 20 * index)
        sleep(delay/20)
    sleep(0.2)
    mouse.up()

#左拖动
def drag_left(w, h, left, top):
    x0 = w * 0.5 + rd() * w * 0.05
    y0 = h * 0.4 + rd() * h * 0.2
    x = x0 - w * 0.2
    y = y0 + rd() * 10 - 5
    drag(x0 + left, y0 + top, x + left, y + top, 0.5)
#右拖动
def drag_right(w, h, left, top):
    x0 = w * 0.5 - rd() * w * 0.05
    y0 = h * 0.4 + rd() * h * 0.2
    x = x0 + w * 0.2
    y = y0 + rd() * 10 - 5
    drag(x0 + left, y0 + top, x + left, y + top, 0.5)
#上拖动
def drag_up(w, h, left, top):
    print rd()
    y0 = h * 0.5 + rd() * h * 0.05
    x0 = w * 0.4 + rd() * w * 0.2
    y = y0 - h * 0.2
    x = x0 + rd() * 10 - 5
    drag(x0 + left, y0 + top, x + left, y + top, 0.5)
#下拖动
def drag_down(w, h, left, top):
    y0 = h * 0.5 - rd() * h * 0.05
    x0 = w * 0.4 + rd() * w * 0.2
    y = y0 + h * 0.2
    x = x0 + rd() * 10 - 5
    drag(x0 + left, y0 + top, x + left, y + top, 0.5)

for index in range(10):
    drag_down(w, h, left, top)
    sleep(0.5)
