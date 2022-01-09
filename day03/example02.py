"""
example02 - 分段函数求值 ---> 构造多分支结构
        3x - 5, x > 1
f（x） = x + 2, -1<= x <= 1
        5x + 3, x< -1

Author: jiuri
Date: 2022/1/6
"""

x = float(input('x = '))
if x > 1:
    y = 3 * x - 5
# 代码越扁平越好
elif x >= -1:
    y = x + 2
else:
    y = 5 * x + 3
print(f'f(x) = {y}')
