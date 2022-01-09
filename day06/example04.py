"""
example04 - 显示所有的汉字

汉字的编码范围：0x4e00 ~ 0x9fa5

Author: jiuri
Date: 2022/1/9
"""

# 把字符转换为编码
print(bin(ord('b')))
print(bin(ord('z')))

print('banana' < 'zoo')
print(ord('王'))
print(ord('骆'))
print('王大锤' < '骆昊')

for i in range(0x4e00, 0x9fa6):
    # chr() ---> 把编码转换为字符
    print(chr(i), end='')
