import math
for T in range(int(input())):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    if x1 == x2 and y1 == y2 and r1 == r2:
        print(-1)
        continue
    if r1 > r2:
        big_x, big_y, big_r, small_x, small_y, small_r = x1, y1, r1, x2, y2, r2
    else:
        big_x, big_y, big_r, small_x, small_y, small_r = x2, y2, r2, x1, y1, r1

    distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    # 외접가능
    if distance > big_r:
        sum_r = r1 + r2
        if sum_r == distance:
            print(1)
        elif sum_r > distance:
            print(2)
        else:
            print(0)
    else:
        flag = distance + small_r
        if flag < big_r:
            print(0)
        elif flag == big_r:
            print(1)
        else:
            print(2)