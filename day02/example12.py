"""
example12 - 输入三角形的三条边的长度，判断能否构成三角形

规则：任意两边和长度大于第三边的长度

Author: jiuri
Date: 2022/1/5
"""

a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
# flag1 = (a + b) > c
# flag2 = (a + c) > c
# flag3 = (b + c) > a
# print(flag1 and flag2 and flag3)
print(a + b > c and b + c > a and a + c > b)
