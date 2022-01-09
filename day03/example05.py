"""
example05 - 

Author: jiuri
Date: 2022/1/6
"""
# 从1到100的范围,101取不到，也可以range(100)
for i in range(1, 101):
    print(i, 'hello, world!')
# 这里警告是因为i是循环变量，离开循环不应该使用，所以警告
print(i, 'goodbye, world!')
