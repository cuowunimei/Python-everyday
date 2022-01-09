"""
example10 - 逻辑运算的应用
and和or两个运算符有短路功能，因此也被称为短路运算符

Author: jiuri
Date: 2022/1/5
"""

a = int(input('a = '))
flag1 = a > 50
flag2 = a % 2 == 0
print(flag1, flag2)
print(flag1 and flag2)
print(a > 50 and a % 2 == 0)
print(a > 50 or a % 2 == 0)
