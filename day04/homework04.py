"""
homework04 - 输入一个正整数，判断它是不是质数（只能被1和自身整除的数）

Author: jiuri
Date: 2022/1/7
"""

num = int(input('请输入一个正整数：'))
is_prime = True
for i in range(2, num):
    if num % i == 0:
        is_prime = False
        break

# 1不是质数
if num > 1 and is_prime:
    print(f'{num}是质数')
else:
    print(f'{num}不是质数')
