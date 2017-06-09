
## vscode中的一些设置
1. python绿色波浪线提醒取消  
在vscode的配置文件里添加如下配置：  
"python.linting.pylintArgs": ["--disable=C,R"]

2. 编码  
#coding=utf-8

3. 没有这个方法的报错屏蔽  
#pylint: disable=maybe-no-member