#coding=utf-8
#pylint: disable=maybe-no-member
import ddxoft.dd as dd
import time

def click(x, y):
    # 进行一次点击
    dd.DD_mov(x, y)
    time.sleep(0.2)
    dd.DD_btn(1)
    time.sleep(0.2)
    dd.DD_btn(2)
    time.sleep(0.2)

def move(x, y):
    dd.DD_mov(x, y)

def down():
    dd.DD_btn(1)

def up():
    dd.DD_btn(2)