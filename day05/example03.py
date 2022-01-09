"""
example03 - 列表的遍历（把每个元素依次取出来）

索引运算（下标运算）- 通过正向或负向索引获取元素

len() ---> length ---> 给出列表中有多少元素

Author: jiuri
Date: 2022/1/8
"""

# 创建列表的字面量语法
nums = [35, 98, 12, 27, 66, 'hello', True, 1 < 2]
nums.pop()
nums.append(78)
nums.append(45)

# print(nums[0], nums[-5])
# print(nums[2], nums[-2])
# print(nums[4], nums[-1])
#
# nums[2] = 120
#
# print(nums)

# # num只是列表元素的代表，只能做读操作
# for num in nums:
#     print(num)
#     num = 100
# print(nums)

# 枚举函数，每次可以取到序号和元素两个值
# 先通过enumerate函数对列表进行预处理
for i, num in enumerate(nums):
    print(i, num)

print('-' * 20)

# 对列表进行读写操作的for循环
for i in range(len(nums)):
    print(nums[i])
    nums[i] = 100
print(nums)

# for i in range(-5, 0):
#     print(nums[i])
