"""
example04 - 乘法口诀表

Author: jiuri
Date: 2022/1/7
"""

n = int(input('n = '))

for i in range(1, n+1):
    for j in range(1, i + 1):
        print(f'{j}*{i}={i * j}', end='\t')
    # 会换两次行
    # print('\n')
    print()
