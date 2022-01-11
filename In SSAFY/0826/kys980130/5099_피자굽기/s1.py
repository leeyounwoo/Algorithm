import sys
sys.stdin = open("input.txt")
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    cheese = list(map(int, input().split()))
    oven = [0] * N
    for i in range(N):
        oven[i] = [cheese[i], i]
    j = 0
    while len(oven) != 1:
        oven[0][0] //= 2
        if oven[0][0] == 0:
            if N+j < M:
                oven.pop(0)
                oven.append([cheese[N+j], N+j])
                j += 1
            else:
                oven.pop(0)
        else:
            oven.append(oven.pop(0))
    print('#{} {}'.format(tc, oven[0][1]+1))
