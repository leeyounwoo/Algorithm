import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    num = list(map(int, input().split()))
    #max, min 초기값을 어떻게 설정할지 생각해보자
    max_num = -1
    min_num = 10000000

    for i in range(N-M+1):
        total = 0
        for j in range(i, i+M):
            total += num[j]

        if max_num < total:
            max_num = total
        if min_num > total:
            min_num = total

    print('#{} {}'.format(tc+1, max_num - min_num))

