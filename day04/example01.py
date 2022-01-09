"""
example01 - 补充练习：输入一个正整数N，将N进行反转

N = 1234
total = 0

1234 // 10 ---> 123 ---> 4
total = total * 10 + 4 ---> 4
123 // 10 ---> 12 ---> 3
total = total * 10 + 3 ---> 43
12 // 10 ---> 1 ---> 2
1 // 10 ---> 0 ---> 1
total = total * 10 + 1 ---> 4321

Author: jiuri
Date: 2022/1/7
"""

N = int(input('N = '))
total = 0

while N != 0:
    total = total * 10 + N % 10
    N //= 10
print(total)
