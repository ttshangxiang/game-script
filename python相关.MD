
## python相关
> 版本：2.7  
## 依赖的包  
1. pip，python包管理工具，相当于npm。
2. opencv-python，图像处理。  
3. pywin32，win32api的python版本。  
4. Pillow，PIL的一个版本，也是一个图像处理工具，我用这个来截图，opencv-python+pywin32，按道理也可以，但是我没写出来。  
5. numpy，opencv-python会依赖这个。  

## 安装这些包
pip没有安装之前，不能使用pip install，或者有些库pip没有，去网上搜安装包，包有exe、tar.gz、whl等种类。  
安装时注意版本中py27、x64、amd64字样。  
exe直接安装，tar.gz解压后，用命令行进入解压目录，运行python setup.py，whl需要使用pip install。  
有了pip之后，可以pip install Pillow这样安装。  
  
pip需要国内镜像，不然完全不能用：
在linux的~目录，windows的用户目录如User/Administrator下创建.pip文件夹，文件夹里面新建pip.conf，windows是pip.ini，内容如下:  
[global]  
trusted-host = mirrors.aliyun.com  
index-url = http://mirrors.aliyun.com/pypi/simple  

## vscode中的一些设置
1. python绿色波浪线提醒取消  
在vscode的配置文件里添加如下配置：  
"python.linting.pylintArgs": ["--disable=C,R"]

2. 编码  
#coding=utf-8

3. 没有这个方法的报错屏蔽  
#pylint: disable=maybe-no-member
