"""
homework01 - 输入三个整数，按照从大到小的顺序输出

Author: jiuri
Date: 2022/1/9
"""

a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))

# if a < b:
#     temp = a
#     a = b
#     b = temp
if a < b:
    a, b = b, a

if a < c:
    a, c = c, a

if c > b:
    b, c = c, b

print(a, b, c)
