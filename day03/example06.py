"""
example06 - 实现1-100求和

Author: jiuri
Date: 2022/1/6
"""

# 直接使用求和函数
print(sum(range(1, 101)))

total = 0
for i in range(1, 101):
    total = total + i
print(total)

# 求1到100的偶数和
total = 0
for i in range(2, 101, 2):
    total = total + i
print(total)

# 求1到100的偶数和
total = 0
for i in range(1, 101):
    if i % 2 == 0:
        total = total + i
    # else:
    #     pass
print(total)
