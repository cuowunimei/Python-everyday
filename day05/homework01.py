"""
homework01 - 猜数字游戏

计算机产生一个1-100的随机数，人输入自己猜的数字
计算机给出对应的提示“大一点”、“小一点”或“恭喜你猜对了”，直到猜中为止。
如果猜的次数超过7次，计算机温馨提示“智商余额明显不足”。

Author: jiuri
Date: 2022/1/7
"""
import random
counter = 0

# shift + F1查询帮助文档
answer = random.randrange(1, 101)
while True:
    counter +=1
    user_answer = int(input('请输入你猜的数字：'))
    if user_answer < answer:
        print('大一点')
    elif user_answer > answer:
        print('小一点')
    else:
        print('恭喜你猜对了')
        break
if counter > 7:
    print('智商余额明显不足')

