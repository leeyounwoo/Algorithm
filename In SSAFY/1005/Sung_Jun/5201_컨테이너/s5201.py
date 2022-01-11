import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    wi = list(map(int, input().split()))
    ti = list(map(int, input().split()))
    used = [1] * len(ti)

    for i in range(len(wi)-1):
        for j in range(i+1, len(wi)):
            if wi[i] < wi[j]:
                wi[i], wi[j] = wi[j], wi[i]
    total = 0
    for num in wi:
        for i in range(len(ti)):
            if used[i] and num <= ti[i]:
                total += num
                used[i] = 0
                break

    print('#{} {}'.format(tc+1, total))
