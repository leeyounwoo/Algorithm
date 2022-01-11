import sys
sys.stdin = open('input.txt')


dx = [1, 1, -1, -1]
dy = [-1, 1, 1, -1]
def dfs(i, j):
    global ans
    stack = [(i, j, i, j, [matrix[i][j]], 0)]

    while stack:
        now_i, now_j, start_i, start_j, cafes, direction = stack.pop()
        # 시작일 때
        if len(cafes) == 1:
            # print('시작', now_i, now_j, start_i, start_j)
            next_i, next_j = now_i + dx[direction], now_j + dy[direction]
            if 0 <= next_i < N and 0 <= next_j < N:
                if matrix[next_i][next_j] not in cafes:
                    no_change_di_cafes = cafes[:]
                    no_change_di_cafes.append(matrix[next_i][next_j])
                    stack.append((next_i, next_j, start_i, start_j, no_change_di_cafes, direction))
                    # print(next_i, next_j, start_i, start_j, no_change_di_cafes, direction)
        # 시작이 아닐 때
        else:
            # 무지성으로 방향 바꿈
            temp_direction = direction + 1
            if temp_direction <= 3:
                next_i, next_j = now_i + dx[temp_direction], now_j + dy[temp_direction]
                if 0 <= next_i < N and 0 <= next_j < N:
                    if matrix[next_i][next_j] not in cafes:
                        change_di_cafes = cafes[:]
                        change_di_cafes.append(matrix[next_i][next_j])
                        stack.append((next_i, next_j, start_i, start_j, change_di_cafes, temp_direction))
                        # print('무지성 바꾸기', next_i, next_j, start_i, start_j, change_di_cafes, temp_direction)
                    elif next_i == start_i and next_j == start_j:
                        if len(cafes) > ans:
                            ans = len(cafes)

            next_i, next_j = now_i + dx[direction], now_j + dy[direction]
            if 0 <= next_i < N and 0 <= next_j < N:
                if matrix[next_i][next_j] not in cafes:
                    not_change_di_cafes = cafes[:]
                    not_change_di_cafes.append(matrix[next_i][next_j])
                    stack.append((next_i, next_j, start_i, start_j, not_change_di_cafes, direction))
                    # print(next_i, next_j, start_i, start_j, not_change_di_cafes, direction)

                elif next_i == start_i and next_j == start_j:
                    if len(cafes) > ans:
                        ans = len(cafes)



for T in range(1, 1+int(input())):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    ans = -1
    for i in range(N):
        for j in range(N):
            dfs(i, j)
    print('#{} {}'.format(T, ans))
