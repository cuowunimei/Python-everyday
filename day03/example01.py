"""
example01 - 分支结构（选择结构）的例子

代码中有多条执行路径，但是只有一条会被执行

admin / Admin123!!

Author: jiuri
Date: 2022/1/5
"""
import getpass

# 制表键在不同系统上空格数可能不同，最好是4个空格
username = input('用户名：')
# pycharm 不支持getpass，Terminal支持
password = getpass.getpass('密码：')
if username == 'admin' and password == 'Admin123!!':
    print('登陆成功！欢迎使用xxx系统！')
    print('欢迎使用xxx系统！')
    print('客服热线：400-800-8800')
else:
    print('登陆失败！')
    print('用户名或密码错误！')
print('程序结束，再见！')
