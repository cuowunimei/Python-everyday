"""
example01 - 列表的切片

Author: jiuri
Date: 2022/1/9
"""

import random

nums = [random.randrange(1, 100) for _ in range(9)]
print(nums)
# 从第三个开始，取后面所有元素
print(nums[2:])
print(nums[:])
print(nums[::])
# 取前面10个元素
print(nums[:10])
print(nums[::-1])
print(nums[1:3])
print(nums[2:7:2])
print(nums[10:15])

# 第二个数字比第一个数字小，返回空
print(nums[5:1])
