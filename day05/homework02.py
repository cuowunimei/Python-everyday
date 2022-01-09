"""
homework02 - 输入10个1-99的整数，计算平均值，找出最大值和最小值

pythonic ---> 跨界程序员

Author: jiuri
Date: 2022/1/8
"""

total = 0
max_value, min_value = 0, 100
for _ in range(10):
    # 15 90
    temp = int(input('请输入：'))
    total += temp
    # 15 > 0 ---> max_value = 15
    # 90 > 15 ---> max_value = 90
    if temp > max_value:
        max_value = temp
    # 15 < 100 ---> min_value = 15
    # 90 > 15 ---> min_value = 15
    if temp < min_value:
        min_value = temp
print(f'平均值：{total / 10}')
print(f'最大值：{max_value}')
print(f'最小值：{min_value}')
