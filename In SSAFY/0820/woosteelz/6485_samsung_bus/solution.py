import sys
sys.stdin = open('input.txt')

TC = int(input())

for tc in range(TC):
    N = int(input())

    bus = []
    for _ in range(N):
        a, b = map(int, input().split())
        bus.append([a, b])

    stops = []
    P = int(input())
    for _ in range(P):
        stop = int(input())
        stops.append(stop)

    ans = [0 for _ in range(P)]

    for i in range(P):
        for j in range(N):
            if bus[j][0] <= stops[i] <= bus[j][1]:
                ans[i] += 1

    print('#{}'.format(tc + 1), *ans)