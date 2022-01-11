import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    N = int(input())
    ai = list(map(int, input().split()))
    max_num = ai[0]
    min_num = ai[0]

    #0번째 인덱스는 이미 비교 했음
    for k in range(1, N):
        if ai[k] > max_num:
            max_num = ai[k]
        elif ai[k] < min_num:
            min_num = ai[k]

    result = max_num - min_num

    print('#{} {}'.format(tc+1, result))
