"""
example06 - 格式化输出

Author: jiuri
Date: 2022/1/4
"""

# 使用input函数从键盘输入数据
# 使用int函数将输入的内容处理成整数（integer）
a = float(input('a = '))
b = float(input('b = '))

print('%.1f + %.1f = %.1f' % (a, b, a + b))
print('%.2f - %.2f = %.2f' % (a, b, a - b))
print('%.1f * %.2f = %.3f' % (a, b, a * b))
print('%f // %f = %f' % (a, b, a // b))
print('%f / %f = %f' % (a, b, a / b))
print('%f %% %f = %f' % (a, b, a % b))
print('%f ** %f = %f' % (a, b, a ** b))
