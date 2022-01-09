"""
example07 -

五个人(ABCDE)晚上去捕鱼，捕了不计其数的鱼，然后累了去睡觉
第二天，A第一个醒过来，把鱼分成了5份，扔掉了多余的一条，然后拿走自己的一份；
B第二个醒过来，以为鱼没有分，包生效的鱼分成了五分，扔掉多余的一条，然后拿走自己的1份；
C、D、E依次醒过来，都按照同样的方法来分鱼。问他们最少捕了多少条鱼？

Author: jiuri
Date: 2022/1/7
"""
fish = 1
while True:
    is_enough = True

    # 检查目前的鱼的数量够不够五个人分
    total = fish
    for _ in range(5):
        if (total - 1) % 5 == 0:
            total = (total - 1) // 5 * 4
        else:
            is_enough = False
            break

    if is_enough:
        print(fish)
        break
    fish += 5
