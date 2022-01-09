"""
example08 - 格式化输出

Author: jiuri
Date: 2022/1/5
"""

# 使用input函数从键盘输入数据
a = float(input('a = '))
b = float(input('b = '))

# f - format - 格式化字符串
print(f'{a} + {b} = {a + b:.2f}')
print(f'{a} - {b} = {a - b:.2f}')
print(f'{a} * {b} = {a * b:.3f}')
print(f'{a} / {b} = {a / b:.4f}')
