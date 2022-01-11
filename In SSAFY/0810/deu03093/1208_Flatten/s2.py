import sys

sys.stdin = open('input.txt')

for T in range(1, 11):
    n = int(input())
    boxs = list(map(int, input().split()))

    ans = 0
    for i in range(n):
        max_box = min_box = boxs[0]
        for box in boxs:
            if max_box < box:
                max_box = box
            if min_box > box:
                min_box = box
        ans = max_box - min_box

        if ans >= 2:
            flag_max = 1
            flag_min = 1
            for j in range(len(boxs)):
                if not flag_max and not flag_min:
                    break
                if flag_max and boxs[j] == max_box:
                    boxs[j] -= 1
                    flag_max = 0
                if flag_min and boxs[j] == min_box:
                    boxs[j] += 1
                    flag_min = 0
        else:
            break
    else:

        max_box = min_box = boxs[0]
        for box in boxs:
            if max_box < box:
                max_box = box
            if min_box > box:
                min_box = box
        ans = max_box - min_box
    print('#{} {}'.format(T, ans))

