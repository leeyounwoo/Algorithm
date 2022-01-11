import sys

sys.stdin = open('input.txt')

for T in range(1, 11):
    n = int(input())
    boxs = list(map(int, input().split()))

    ans = 0
    for i in range(n):
        max_box = max(boxs)
        min_box = min(boxs)
        ans = max_box - min_box

        if ans >= 2:
            max_index = boxs.index(max_box)
            min_index = boxs.index(min_box)
            boxs[max_index] -= 1
            boxs[min_index] += 1
        else:
            break
    # 마지막 if ans >= 2절이 의미가 있을 때 틀리게 됩니다.
    else:
        max_box = max(boxs)
        min_box = min(boxs)
        ans = max_box - min_box
    print('#{} {}'.format(T, ans))

