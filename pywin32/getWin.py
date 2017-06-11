#coding=utf-8
#pylint: disable=maybe-no-member
'''
获取窗口
'''
import win32gui, win32con
def callback(hwnd, extra):
    text = win32gui.GetWindowText(hwnd).decode('mbcs').encode('utf-8')
    if (extra['find'] in text):
        extra['hwnd'] = hwnd
        extra['text'] = text

def getWindow(str):
    obj = {'find': str, 'hwnd': None}
    win32gui.EnumWindows(callback, obj)
    return obj['hwnd']
