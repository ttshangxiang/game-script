#coding=utf-8
#pylint: disable=maybe-no-member
'''
获取窗口的图片
'''
import getWin
import win32gui
from PIL import ImageGrab

hwnd = getWin.getWindow('Bluestacks')
win32gui.SetForegroundWindow(hwnd)
left, top, right, bottom = win32gui.GetWindowRect(hwnd)

im = ImageGrab.grab((left, top, right, bottom))
im.save('D:\\a.jpg','jpeg')