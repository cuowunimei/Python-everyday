"""
example07 - 求1-100之间3或5的倍数的和

Author: jiuri
Date: 2022/1/6
"""

total = 0
for i in range(1, 16):
    if i % 3 == 0 or i % 5 == 0:
        total = total + i
print(total)
