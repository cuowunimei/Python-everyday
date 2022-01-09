"""
homework05 - 输入三角形三条边的长度，如果能构成三角形就计算周长和面积，
如果不能构成三角形，提示用户重新输入，直到正确。

Author: jiuri
Date: 2022/1/7
"""
import math

while True:
    a = float(input('a = '))
    b = float(input('b = '))
    c = float(input('c = '))
    if a + b > c and b + c > a and a + c > b:
        perimeter = a + b + c
        half = perimeter / 2
        # 海伦公式
        # sqrt ---> square root
        # area =math.sqrt(half * (half - a) * (half - b) * (half - c)
        area = (half * (half - a) * (half - b) * (half - c)) ** 0.5
        print(f'三角形的周长为：{perimeter:.2f}')
        print(f'三角形的面积为：{area:.2f}')
        break
    else:
        print('不能构成三角形，请重新输入！')
