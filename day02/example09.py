"""
example09 - Python中的运算符

~ 赋值运算符： 右边的值赋给左边（变量） ---> =
~ 算术运算符 ---> + - * / // % **
~ 复合的赋值运算符 ---> =+ -= *= /= ...
~ 关系运算符（比较运算符） ---> > < >= <= == !=
~ 逻辑运算符： 把多个布尔值处理成一个布尔值（多个布尔值的组合） ---> and（与） / or（或） / not（非）
Author: jiuri
Date: 2022/1/5
"""

print(True and False)
print(True and True)
print(False and False)
print(False and True)
print('-' * 10)
print(True or False)
print(True or True)
print(False or False)
print(False or True)
print('-' * 10)
print(not True)
print(not False)

a = 5
b = 3
# a = a+b
a += b
# a = a * (b + 2)
a *= b + 2
print(a)
print(a > b)
print(a != b)
print(a <= b)
