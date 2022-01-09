"""
example01 - 将一粒骰子掷60000次，统计每一面出现的次数

升级版：将两颗色子摇1000次，统计每一面出现的次数

import random

random.randrange(1, 7) ---> 用1-6的随机数模拟骰子

运算符 ---> 优先级和结合性

左结合：从左向右进行计算（大部分运算符）
右结合：从右向左进行计算（赋值运算符，正负号，索引和切片）

Author: jiuri
Date: 2022/1/8
"""
import random

# f1, f2, f3, f4, f5, f6 = 0
f1 = f2 = f3 = f4 = f5 = f6 = f7 = f8 = f9 = f10 = f11 = f12 = 0
for _ in range(60000):
    face1 = random.randrange(1, 7)
    face2 = random.randrange(1, 7)
    face = face1 + face2
    if face == 1:
        f1 += 1
    elif face == 2:
        f2 += 1
    elif face == 3:
        f3 += 1
    elif face == 4:
        f4 += 1
    elif face == 5:
        f5 += 1
    elif face == 6:
        f6 += 1
    elif face == 7:
        f7 += 1
    elif face == 8:
        f8 += 1
    elif face == 9:
        f9 += 1
    elif face == 10:
        f10 += 1
    elif face == 11:
        f11 += 1
    else:
        f12 += 1
print(f'1点摇出了{f1}次')
print(f'2点摇出了{f2}次')
print(f'3点摇出了{f3}次')
print(f'4点摇出了{f4}次')
print(f'5点摇出了{f5}次')
print(f'6点摇出了{f6}次')
print(f'7点摇出了{f7}次')
print(f'8点摇出了{f8}次')
print(f'9点摇出了{f9}次')
print(f'10点摇出了{f10}次')
print(f'11点摇出了{f11}次')
print(f'12点摇出了{f12}次')
