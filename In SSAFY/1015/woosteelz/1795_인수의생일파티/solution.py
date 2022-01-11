T = int(input())
for tc in range(1, T + 1):
    N, M, X = map(int, input().split())

    adj1 = [[float('inf')] * (N + 1) for _ in range(N + 1)]
    adj2 = [[float('inf')] * (N + 1) for _ in range(N + 1)]

    for _ in range(M):
        x, y, c = map(int, input().split())
        adj1[x][y] = c
        adj2[y][x] = c

    dist1 = [float('inf')] * (N + 1)
    dist2 = [float('inf')] * (N + 1)

    max_value = 0

    for i in range(1, N+1):
        if dist1[i] + dist2[i] > max_value:
            max_value = dist1[i] + dist2[i]

    print("#{} {}".format(tc, max_value))
