import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    a = list(map(int, input()))
    result = [0 for _ in range(10)]
    for i in a:
        result[i] += 1

    max_card = max(result)
    max_idx = 0
    for i in range(len(result)):
        if max_card == result[i]:
            max_idx = i

    print('#{} {} {}'.format(tc, max_idx, max_card))








