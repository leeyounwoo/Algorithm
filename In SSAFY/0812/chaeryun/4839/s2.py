import sys
sys.stdin = open("input.txt")

T = int(input())


def binarysearch(P, Pa):
    L = 1
    R = P
    count = 1

    center = (L + R) // 2

    while center != Pa:
        count += 1
        if center < Pa:
            L = center  # 시작값을 center로 바꿔줌
        else:
            R = center  # 마지막값을 center로 바꿔줌
        center = (L + R) // 2

    return count

for i in range(1, T + 1):
    P, Pa, Pb = map(int, input().split())
    count_A = binarysearch(P, Pa)
    count_B = binarysearch(P, Pb)

    if count_A < count_B:
        print('#{} A'.format(i))
    elif count_A == count_B:
        print('#{} 0'.format(i))
    else:
        print('#{} B'.format(i))