import sys
sys.stdin = open('input.txt')


def permutation(N, graph, k):

    global result
    global order

    if k == N:
        total_cost = 0
        for i in range(N-1):
            total_cost += graph[order[i]][order[i+1]]
        total_cost += graph[order[N-1]][order[0]]
        if result > total_cost:
            result = total_cost
    else:
        for i in range(k, N):
            order[i], order[k] = order[k], order[i]
            permutation(N, graph, k+1)
            order[i], order[k] = order[k], order[i]


T = int(input())

answer = []
for tc in range(1, T + 1):

    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]

    result = 100000000
    order = list(range(N))
    # 0, 1, 2,..., N-1

    permutation(N, graph, 1)

    answer.append(result)

for tc in range(1, T+1):
    print(f'#{tc} {answer[tc-1]}')
