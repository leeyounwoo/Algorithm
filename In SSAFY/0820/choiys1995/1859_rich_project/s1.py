import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    cost = list(map(int, input().split()))

    ans = 0

    for i in range(N-1): # 마지막은 안사도 그만이다
        max_cost = cost[i]
        for j in range(i+1, N):
            if max_cost < cost[j]:
                max_cost = cost[j]

        if max_cost > cost[i]:
            ans += max_cost - cost[i] # 이익

    print('#{} {}'.format(tc, ans))