"""
homework02 - 向列表中添加10个随机整数，找出其中第2大的元素
[a, b) ---> random.random() * (b - a) + a
    # 100到200，不包括两百的随机小数
    temp = random.random() * 100 + 100
Author: jiuri
Date: 2022/1/9
"""
import random

nums = []
# 列表的生成式（推导式）---> 写法简明，效率更高
nums = [random.randrange(1, 100) for _ in range(1000)]
nums = [i for i in range(1, 101, 2)]

# for _ in range(10):
#     temp = random.randrange(1, 100)
#     nums.append(temp)
# print(nums)

# max_value = max(nums)
# # 通过remove操作从列表中删除指定的元素
# nums.remove(max_value)
# print(max(nums))

# max_value = nums[0]
# for i in range(1, len(nums)):
#     if nums[i] > max_value:
#         max_value = nums[i]
# print(max_value)

m1, m2 = nums[0], nums[1]
if m1 < m2:
    m1, m2 = m2, m1
for i in range(2, len(nums)):
    if nums[i] > m1:
        m1, m2 = nums[i], m1
    elif nums[i] == m1:
        pass
    elif nums[i] > m2:
        m2 = nums[i]
print(m1, m2)
