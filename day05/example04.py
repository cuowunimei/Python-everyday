"""
example04 - 将一粒骰子掷60000次，统计每一面出现的次数

Author: jiuri
Date: 2022/1/8
"""
import random

fs = [0, 0, 0, 0, 0, 0]
# fs = [0] * 6

for _ in range(60000):
    face = random.randrange(1, 7)
    fs[face - 1] += 1

for i, value in enumerate(fs):
    print(f'{i + 1}点摇出了{value}次')
