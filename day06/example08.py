"""
example08 - 随机抽取和乱序

Author: jiuri
Date: 2022/1/10
"""
import random

names = [
    '王浪', '项宇', '殷雨', '王勇', '潘盛辉', '夏红霞', '陈绩',
    '范青青', '余翠', '龚凡', '邓采虎', '缪国庆', '王卫东'
]

print(len(names))
# sample函数可以对列表元素无放回随机抽样
print(random.sample(names, k=5))
# choices函数可以对列表元素进行有放回抽样（可以重复抽中）
print(random.choices(names, k=5))
# choice函数可以从列表中随机选择一个元素
print(random.choice(names))
# shuffle函数可以实现列表元素的随即乱序，原地打乱
random.shuffle(names)
print(names)
