import sys
sys.stdin = open('input.txt')


def binary_search(page, target):
    left = 1
    right = page
    cnt = 0
    while left <= right:
        middle = (left + right) // 2
        cnt += 1

        if middle == target:
            return cnt
        elif middle < target:
            left = middle
        else:
            right = middle


T = int(input())
for tc in range(1, T+1):
    p, target_a, target_b = map(int, input().split())

    result_a = binary_search(p, target_a)
    result_b = binary_search(p, target_b)

    print('#{} '.format(tc), end='')
    if result_a < result_b:
        print('A')
    elif result_a > result_b:
        print('B')
    else:
        print(0)