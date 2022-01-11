import sys
sys.stdin = open('input.txt')


def cost(X, Y, i, j, E):
    return E * ((abs(X[i] - X[j]) ** 2) + (abs(Y[i] - Y[j]) ** 2))


def kruskal(N, edges):
    def find_set(x):
        if parents[x] != x:
            parents[x] = find_set(parents[x])
        return parents[x]

    def union(x, y):
        root_x = find_set(x)
        root_y = find_set(y)
        if root_x == root_y:
            return False

        if ranks[root_x] > ranks[root_y]:
            parents[root_y] = root_x
        else:
            parents[root_x] = root_y
            if ranks[root_x] == ranks[root_y]:
                ranks[root_y] += 1

        return True

    edges.sort(key=lambda x: x[2])

    parents = [i for i in range(N)]
    ranks = [0 for _ in range(N)]

    count = 0
    result = 0
    while count < N - 1:
        u, v, cost = edges.pop(0)
        if union(u, v):
            count += 1
            result += cost

    return result


T = int(input())

answer = []
for tc in range(1, T + 1):

    N = int(input())

    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    E = float(input())

    edges = []
    for i in range(N - 1):
        for j in range(i + 1, N):
            edges.append([i, j, cost(X, Y, i, j, E)])

    result = round(kruskal(N, edges))
    answer.append(result)

for tc in range(1, T + 1):
    print(f'#{tc} {answer[tc-1]}')