"""
example03 - 数字矩阵

Author: jiuri
Date: 2022/1/7
"""

n = int(input('n = '))

for i in range(1, n+1):
    for j in range(1, i + 1):
        print(i, end=' ')
    # 会换两次行
    # print('\n')
    print()
