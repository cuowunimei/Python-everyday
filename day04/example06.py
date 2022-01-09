"""
example06 - 百钱百鸡问题

鸡翁一，值钱五；鸡母一，值钱三；鸡雏三，值钱一；
百钱买百鸡，则翁、母、雏各几何？

穷举法：穷尽所有的可能行，然后设置条件，找到问题的解 ---> 暴力破解法

Author: jiuri
Date: 2022/1/7
"""

for x in range(0, 21):
    for y in range(0, 34):
        for z in range(0, 100, 3):
            if x + y + z == 100 and 5 * x + 3 * y + z // 3 == 100:
                print(x, y, z)

# 优化代码,减少循环次数
for x in range(0, 21):
    for y in range(0, 34):
        z = 100 - x - y
        if z % 3 == 0 and 5 * x + 3 * y + z // 3 == 100:
            print(x, y, z)
