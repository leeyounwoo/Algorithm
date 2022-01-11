import sys
sys.stdin = open('input.txt')


def arr_min_sum(i, tmp):
    global result
    if i == N:
        result = min(result, tmp)
    if tmp > result:
        return

    for j in range(N):
        if visited[j] == 0:
            visited[j] = 1
            arr_min_sum(i+1, tmp+arr[i][j])
            visited[j] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 1000
    visited = [0] * N

    arr_min_sum(0, 0)

    print('#{} {}'.format(tc, result))