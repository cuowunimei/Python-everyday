"""
example02 - 容器型数据变量（用一个变量可以保存多个数据）

~ 列表（list）
~ 元组（tuple）
~ 集合（set）
~ 字典（dict）

Author: jiuri
Date: 2022/1/8
"""
# 用复数形式表示多个值
# C语言最后不能乱加逗号
nums = [10, 100, 1000, ]
print(type(nums))
rules = ['热爱祖国，热爱人们', '尊敬师长，团结同学',
         '好好学习，天天向上',
         '爱惜公共财物，不得在公共区域大声喧哗'
         ]
print(rules)
print(type(rules))

# append ---> 追加
nums.append(10000)
# 在第一个之前加上1
nums.insert(0, 1)
print(nums)

# 去除最后一个元素
rules.pop()
print(rules)
