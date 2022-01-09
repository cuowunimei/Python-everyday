"""
example02 - 分段函数求值 ---> 构造多分支结构
        3x - 5, x > 1
f（x） = x + 2, -1<= x <= 1
        5x + 3, x< -1

分支结构可以嵌套使用，但一定要注意嵌套深度，嵌套深度太深直接影响代码可读性

代码块：保持相同所进的代码就属于同一个代码块

Author: jiuri
Date: 2022/1/6
"""

x = float(input('x = '))
if x > 1:
    y = 3 * x - 5
else:
    if x < -1:
        y = 5 * x + 3
    else:
        y = x + 2
print(f'f(x) = {y}')
