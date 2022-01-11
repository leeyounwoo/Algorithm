def powerset(mat, visited, y, total):
    global result

    # 가지치기 (현재까지의 합이 최소값보다 큰 경우)
    if total > result:
        return

    # 마지막 행에 도달했을 경우
    if y == N:
        if total <= result:
            result = total
        return

    for x in range(N):
        if visited[x] == 0:  # 같은 열에 있는 원소를 고르지 않기 위해
            visited[x] = 1   # 현재 열 체크
            powerset(mat, visited, y+1, total+mat[y][x])
            visited[x] = 0


T = int(input())
for tc in range(1, 1 + T):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]

    result = 98765321
    visited = [0] * N
    powerset(mat, visited, 0, 0)
    print('#{} {}'.format(tc, result))
