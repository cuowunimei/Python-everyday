"""
example03 - 列表的相关操作

Author: jiuri
Date: 2022/1/9
"""

items = ['banana', 'grape', 'apple', 'waxberry', 'pitaya', 'apple']

if 'waxberry' in items:
    print(items.index('waxberry'))
if 'apple' in items:
    print(items.index('apple'))
# 从索引为三（不是序列，直接是第三个元素的位置）开始找
if 'apple' in items[3:]:
    print(items.index('apple', 3))

# count() ---> 判断元素在列表中出现的次数
print(items.count('apple'))

# 添加元素
items.append('blueberry')
# 在一号的前面插入
items.insert(1, 'watermelon')
print(items)

# 删除元素
# pop会返回删除的元素
temp = items.pop()
print(temp)
items.pop(4)
# del ---> 删除对象的引用
del items[0]
print(items)
# 从列表中删除第一次出现的元素
# 删除所有 'apple'
while 'apple' in items:
    items.remove('apple')
print(items)

# 清空列表元素
items.clear()
print(items)
