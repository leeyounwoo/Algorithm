import sys
sys.stdin = open('input.txt')

T = 10
for _ in range(1, T + 1):
    tc, N = map(int, input().split())

    G = [[0] * 100 for _ in range(100)]
    E = list(map(int, input().split()))
    for i in range(N):
        r_a, r_b = E[2 * i], E[2 * i + 1]
        G[r_a][r_b] = 1

    stack = [0]
    visited = [0] * 100

    while stack: #stack이 안 비어 있을 때까지
        v = stack.pop() # 현재 방문하려는 노드
        if not visited[v]:  # 내가 방문하려는 노드에 한 번도 방문하지 않았으면
            visited[v] = 1 # 방문표기

        for w in range(100):
            if G[v][w] == 1 and visited[w] == 0:
                stack.append(w)

    if visited[99]:
        print('#{} {}'.format(tc, 1))
    else:
        print('#{} {}'.format(tc, 0))