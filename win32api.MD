

[win32api文档](http://www.esk365.com/zxsc/prg/winapia/)  
[pywin32文档](http://timgolden.me.uk/pywin32-docs/contents.html)  

## 未解之谜

1. 无法通过窗口标题查找到窗口
win32gui.FindWindow(None, 'a.txt')，无论如何都返回0

## 以解之谜

1. 遍历窗口时，输出的窗口标题中文是乱码问题  
原因是返回的编码是mbcs，转一下就可以，详情见[文档](http://timgolden.me.uk/pywin32-docs/win32gui__GetWindowText_meth.html)
```python
def callback(hwnd, extra):
    extra.append(hwnd)
    print win32gui.GetClassName(hwnd)
    print win32gui.GetWindowText(hwnd).decode('mbcs')

window = []
win32gui.EnumWindows(callback, window)
print window

```