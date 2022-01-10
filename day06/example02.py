"""
example02 - 列表的相关操作

Author: jiuri
Date: 2022/1/9
"""

# 创建列表的方式一：字面量语法
list1 = ['apple', 'orange', 'pitaya', 'durian']
# list2 = list('abcdefg')
# list2 = list(list1)
# 创建列表的方式二：构造器语法
list2 = list(range(1, 10))
print(list2)
# 创建列表的方式三：生成式（推导式语法）
list3 = [i ** 2 for i in range(1, 10)]
print(list3)

# 获取列表元素的个数 ---> len()
print(len(list1))
print(len(list3))

# 遍历列表中的元素
for i in range(len(list1)):
    print(list1[i])
# 负向索引
for i in range(-len(list1), 0):
    print(list1[i])

for x in list1:
    print(x)

for i, x in enumerate(list1):
    print(i, x)

# 和列表相关的运算
# 重复运算
list4 = [1, 10, 100] * 5
print(list4)

# 成员运算，成员在不在列表中，返回布尔值
print(10 in list4)
print(5 not in list4)
print('pitaya' in list1)
print('grape' in list1)

# 索引和切片
# 正向索引：0 ~ N-1 / 负向索引：-N ~ -1

# 合并
list5 = [1, 3, 5, 7]
list6 = [4, 4, 8]
# list6 += list5
# 列表五的结果合并到列表六中
list6.extend(list5)
print(list6)

# 比较
list7 = list(range(1, 8, 2))
list8 = [0, 3, 5, 7, 9]
# 比较两个列表的元素是否意义对应相等
print(list5 == list7)
print(list7 == list8)
# 比较两个列表对应元素的大小
print(list7 > list8)
