#coding=utf-8
#pylint: disable=maybe-no-member
'''
发送鼠标键盘事件
'''
import ctypes
import time
import os

path = os.path.split(os.path.realpath(__file__))[0]
dd_dll = ctypes.cdll.LoadLibrary(path + '\dd71800x64.64.dll')

# DD虚拟码，可以用DD内置函数转换。
vk = {'5': 205, 'c': 503, 'n': 506, 'z': 501, '3': 203, '1': 201, 'd': 403, '0': 210, 'l': 409, '8': 208, 'w': 302,
        'u': 307, '4': 204, 'e': 303, '[': 311, 'f': 404, 'y': 306, 'x': 502, 'g': 405, 'v': 504, 'r': 304, 'i': 308,
        'a': 401, 'm': 507, 'h': 406, '.': 509, ',': 508, ']': 312, '/': 510, '6': 206, '2': 202, 'b': 505, 'k': 408,
        '7': 207, 'q': 301, "'": 411, '\\': 313, 'j': 407, '`': 200, '9': 209, 'p': 310, 'o': 309, 't': 305, '-': 211,
        '=': 212, 's': 402, ';': 410}
# 需要组合shift的按键。
vk2 = {'"': "'", '#': '3', ')': '0', '^': '6', '?': '/', '>': '.', '<': ',', '+': '=', '*': '8', '&': '7', '{': '[', '_': '-',
        '|': '\\', '~': '`', ':': ';', '$': '4', '}': ']', '%': '5', '@': '2', '!': '1', '(': '9'}

def key(code):
    # 进行一组按键。

    dd_dll.DD_key(vk[code], 1)
    time.sleep(0.2)
    dd_dll.DD_key(vk[code], 2)

def click(x, y):
    # 进行一次点击
    dd_dll.DD_mov(x, y)
    time.sleep(0.2)
    dd_dll.DD_btn(1)
    time.sleep(0.2)
    dd_dll.DD_btn(2)
    time.sleep(0.2)

def keyDown(code):
    dd_dll.DD_key(vk[code], 1)

def keyUp(code):
    dd_dll.DD_key(vk[code], 2)

def move(x, y):
    print x, y
    dd_dll.DD_mov(x, y)

def down():
    dd_dll.DD_btn(1)

def up():
    dd_dll.DD_btn(2)
