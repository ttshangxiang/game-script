

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

2. 窗口截图

[链接](http://www.upgradeyourtechlife.com/blog/?p=82)

2. 无法发送鼠标键盘事件到安卓模拟器
无论是用SendMessage还是mouse_event，autopy，安卓模拟器都受到了屏蔽，有人说需要驱动级别的输入，找到了这个  
[ddxoft](http://www.ddxoft.com/)，发现可以用，感谢！！  
试了大漠插件没有试出来，大漠插件有后台找图和后台键鼠的功能，希望能把他用出来。  
win32api被限制挺大的  