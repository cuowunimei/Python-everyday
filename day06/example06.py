"""
example06 - 排序

简单选择排序 - 每次从剩下的元素中选择最小的

Author: jiuri
Date: 2022/1/9
"""

nums = [35, 12, 99, 58, 67, 42, 49, 31, 73]

# sorted_nums = []
# while len(nums) > 0:
#     min_value = min(nums)
#     sorted_nums.append(min_value)
#     nums.remove(min_value)
# print(sorted_nums)

# 最后一个就是最大值
for i in range(len(nums) - 1):
    # 假设第一个元素就是最小值
    min_value, min_index = nums[i], i
    # 通过循环寻找有没有更小的值并记下它的位置和值
    for j in range(i + 1, len(nums)):
        if nums[j] < min_value:
            min_index = j
            min_value = nums[j]
    # 将最小的值换到最前面的位置
    nums[i], nums[min_index] = nums[min_index], nums[i]
print(nums)
