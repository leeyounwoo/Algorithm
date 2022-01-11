import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    edges = list(map(int, input().split()))
    adj_mat = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
    result = []
    cnt = 0
    adj_list = {x: [] for x in range(1, N + 1)}
    for i in range(0, len(edges) - 1, 2):
        s, e = edges[i], edges[i + 1]
        adj_list[s].append(e)
    for j in range(1, N+1):
        if adj_list[j] != []:
            cnt += 1
            for k in adj_list[j]:
                if k in range(1, N+1):
                    cnt -= 1
        else:
            cnt += 1
    print('#{} {}'.format(tc, cnt))