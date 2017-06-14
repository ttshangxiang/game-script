#coding=utf-8
#pylint: disable=maybe-no-member

'''
场景：章节
动作：
上一章
下一章
战役
关卡选择
'''

def judgeScene():
    if '找到图片':
        return True
    return False

def judgeChapter():
    print '判断现在是第几章'

def prevChapter():
    print '上一章'

def nextChapter():
    print '下一章'

def next(chapter):
    print '进入章节'

def enterBattle():
    print '进入战役'