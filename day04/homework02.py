"""
homework02 - 找到1~10000之间的完美数（除自身外所有因子的和等于这个数）

6 = 1 + 2 + 3
28 = 1 + 2 + 4 + 7 + 14

Author: jiuri
Date: 2022/1/7
"""
import time
import math

start = time.time()
for num in range(2, 1000000):
    total = 1
    # 优化程序，数量级开根号
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            total += i
            if i != num // i:
                total += num // i

    if num == total:
        print(num)
end = time.time()
print(f'执行时间:{end - start:.3f}秒')
