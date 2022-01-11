import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    V, E = map(int, input().split())

    test_list = [[0]*(V+1) for _ in range(V+1)]
    visited = [0]*(V+1)

    for _ in range(E):
        nod, nx_nod = map(int, input().split())
        test_list[nod][nx_nod] = 1
        test_list[nx_nod][nod] = 1

    start, end = map(int, input().split())
    stack = []
    stack.append(start)

    result = []
    while stack:
        v = stack.pop()
        result.append(v)

        if visited[v] == 0:
            visited[v] = 1
            for w in range(1, V+1):
                if test_list[v][w] == 1 and visited[w] == 0:
                    stack.append(w)

    final = 1
    for num in [start, end]:
        if num not in result:
            final = 0
    print('#{} {}'.format(tc+1, final))





