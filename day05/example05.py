"""
example05 - 输入十个整数，计算平均值、方差和标准差，找出最大值和最小值

Author: jiuri
Date: 2022/1/8
"""

nums = []
for _ in range(10):
    temp = int(input('请输入数据：'))
    nums.append(temp)
print(nums)
mean_value = sum(nums) / len(nums)

total = 0
for num in nums:
    total += (num - mean_value) ** 2
# 方差 ---> variance ---> var
var_value = total / (len(nums) - 1)
# 标准差 ---> standard deviation ---> std / stdev
std_value = var_value ** 0.5
max_value = max(nums)
min_value = min(nums)
print(f'均值：{mean_value}')
print(f'方差：{var_value}')
print(f'标准差：{std_value}')
print(f'极差(全距)：{max_value - min_value}')
