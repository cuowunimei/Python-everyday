"""
输入两个整数进行算术运算

Author: jiuri
Date: 2022年1月4日
"""

# 使用input函数从键盘输入数据
# 使用int函数将输入的内容处理成整数（integer）
a = int(input('a = '))
b = int(input('b = '))

print(a + b)
print(a - b)
print(a * b)
# 整除法（除法运算的结果没有小数）
print(a // b)
print(a / b)
print(a % b)
# 求幂（计算123的45次方）
print(a ** b)
