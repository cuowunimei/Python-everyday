"""
example04 - 个人所得税（旧版）计算器

Author: jiuri
Date: 2022/1/6
"""

total = float(input('本月收入：'))
insurance = float(input('五险一金扣除：'))
E = total - insurance
# 名为I、O和l的变量可能很难读懂。这是因为字母I和字母l很容易混淆，字母O和数字0也很容易混淆，所以这里报错
I = E - 3500

# 上述程序在执行时，首先执行if语句，如果成立，则下面的elif和else语句都将被忽略；如果不成立，则执行elif语句；如果elif语句仍不成立，则执行最后的else语句
if 0 < I <= 1500:
    R = 0.03
    D = 0
elif I <= 4500:
    R = 0.1
    D = 105
elif I <= 9000:
    R = 0.2
    D = 555
elif I <= 35000:
    R = 0.25
    D = 1005
elif I <= 55000:
    R = 0.3
    R = 2755
elif I <= 80000:
    R = 0.35
    D = 5505
else:
    R = 0.45
    D = 13505

if I > 0:
    T = I * R - D
else:
    T = 0

print(f'应纳税款：{T:.2f}元')
print(f'税后收入：{E - T:.2f}元')
