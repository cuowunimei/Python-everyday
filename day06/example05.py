"""
example05 - 列表的操作（反转和排序）

Author: jiuri
Date: 2022/1/9
"""

items = ['banana', 'grape', 'apple', 'waxberry', 'pitaya', 'apple']
print(items[::-1])
# items = items[::-1]
# 在列表直接反转
items.reverse()
print(items)

# 排序（可以修改reverse参数控制排升序或者排降序)，默认从小到大
items.sort(reverse=True)
print(items)

nums = ['1', '10', '234', '2', '35', '100']
nums.sort()
print(nums)
# 按整数的方法排序
nums.sort(key=int)
print(nums)

# nums2 = [int(num) for num in nums]
# nums2.sort()
# print(nums2)
# nums3 = [str(num) for num in nums2]
# print(nums3)
