import sys
sys.stdin = open('input.txt')

def bfs(v):
    cnt = [0]*(V+1)
    queue = [v]

    while queue:
        v = queue.pop(0)
        visited[v] = 1

        for w in range(1, V+1):
            if arr[v][w] == 1 and visited[w] == 0:
                queue.append(w)
                if cnt[w] and cnt[w] > cnt[v]+1:
                    cnt[w] = cnt[v] + 1
                elif not cnt[w]:
                    cnt[w] = cnt[v] + 1

    return cnt[G]


T = int(input())

for t in range(1, T+1):
    V, E = map(int, input().split())

    arr = [[0]*(V+1) for _ in range(V+1)]
    visited = [0] * (V + 1)

    for _ in range(E):
        i, j = map(int, input().split())
        arr[i][j] = 1
        arr[j][i] = 1

    S, G = map(int, input().split())

    print('#{} {}'.format(t, bfs(S)))