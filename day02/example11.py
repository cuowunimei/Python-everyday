"""
example11 - 输入一个年份，判断这个年份是不是闰年

规则：四年一闰，百年不闰，四百年又闰

Author: jiuri
Date: 2022/1/5
"""

year = int(input('请输入年份：'))
# flag1 = year % 4 == 0
# flag2 = year % 100 != 0
# flag3 = year % 400 == 0
# print(flag1 and flag2 or flag3)
print(year % 4 == 0 and year % 100 != 0 or year % 400 == 0)
