"""
example02 - 打印出1-100范围内的质数

Author: jiuri
Date: 2022/1/7
"""

for num in range(2, 100):
    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num, end=',')
