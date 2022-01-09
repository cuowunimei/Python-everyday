"""
example09 - 输入一个非负整数N，计算N！
N！ = N * （N - 1） * (N - 2) * ... * 2 * 1

Author: jiuri
Date: 2022/1/7
"""

n = int(input('n = '))
total = 1
for i in range(2, n + 1):
    total *= i
print(f'{n} != {total}')
