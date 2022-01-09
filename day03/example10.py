"""
example10 - 输入两个正整数，找出他们的最大公约数

如果数a能被数b整除，a就叫做b的倍数，b就叫做a的约数。
最大公因数，也称最大公约数、最大公因子，指两个或多个整数共有约数中最大的一个。
(greatest common divisor)

bug ---> 缺陷 / 故障 / 问题 ---> debug（调试）

Author: jiuri
Date: 2022/1/6
"""

x = int(input('x = '))
y = int(input('y = '))

# 欧几里得算法(辗转相除法)
while y % x != 0:
    # temp = y
    # y = x
    # x = temp % x
    x, y = y % x, x
print(x)

for i in range(x, 0, -1):
    if x % i == 0 and y % i == 0:
        print(i)
        break
