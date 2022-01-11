import sys

sys.stdin = open('input.txt')

for test_case in range(1, 11):
    land = int(input())
    genmul = list(map(int, input().split()))
    result = 0

    for idx in range(2, land - 2):
        big_height = genmul[idx]
        left = max(genmul[idx - 2:idx])
        right = max(genmul[idx + 1: idx + 3])

        if left > big_height or right > big_height:
            continue

        result += big_height - max(left, right)
    print(f'# {test_case} {result}')

