"""
homework01 - 找出100~999之间的水仙花数（各位数字的立方和刚好等于这个数本身）


153 = 1^3 + 5^3 + 3^3

123 // 100 = 1 ---> 23
123 % 10 = 12 ---> 3
567 // 100 = 5 ---> 67
567 % 10 =56 ---> 7

Author: jiuri
Date: 2022/1/7
"""

for num in range(100, 1000):
    hundreds_digit = num // 100
    ten_digit = num // 10 % 10
    units_digit = num % 10
    if hundreds_digit ** 3 + ten_digit ** 3 + units_digit ** 3 == num:
        print(num)
