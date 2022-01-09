"""
homework03 - 输入两个非负整数m和n（m >=n）, 计算C(m, n)的值

A(m, n) = m! / (m - n)! ---> 排列 ---> permutation
C(m, n) = m! / n! / (m - n)! ---> 组合 ---> combination

C(5 , 3) = 5! / 3 ! / 2! = 10

as ---> alias --->别名

Author: jiuri
Date: 2022/1/7
"""
# import math
from math import factorial as f

m = int(input('m = '))
n = int(input('n = '))

# fm = 1
# for i in range(2, m + 1):
#     fm *= i
#
# fn = 1
# for i in range(2, n + 1):
#     fn *= i
#
# fk = 1
# for i in range(2, m - n + 1):
#     fk *= i

# 阶乘函数
fm = f(m)
fn = f(n)
fk = f(m - n)

print(fm // fn // fk)
