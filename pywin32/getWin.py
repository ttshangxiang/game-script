#coding=utf-8
#pylint: disable=maybe-no-member
'''
获取窗口
'''
import win32gui, win32con
def callback(hwnd, extra):
    text = win32gui.GetWindowText(hwnd).decode('mbcs').encode('utf-8')
    print text
    if ('关闭窗口' in text):
        print '------------'
        win32gui.PostMessage(hwnd, win32con.WM_CLOSE, 0, 0)

window = []
win32gui.EnumWindows(callback, window)
print window
