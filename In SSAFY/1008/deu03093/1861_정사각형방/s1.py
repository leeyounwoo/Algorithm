import sys
sys.stdin = open('input.txt')

# dp로 풀어야 할듯

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
def dfs(i, j, max_num, count, pi, pj):
    global ans_count, ans_value
    if ans_count < count:
        ans_count = count
        ans_value = max_num

    check[i][j] = True
    # print(i, j, max_num, count, pi, pj)
    next_count = count + 1
    for temp in range(4):
        ni, nj = i + dx[temp], j + dy[temp]
        if 0 <= ni < N and 0 <= nj < N and matrix[ni][nj] == max_num + 1:
            if check[ni][nj] == False:
                dfs(ni, nj, matrix[ni][nj], next_count, i, j)


for T in range(1, 1+int(input())):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    # print(check)
    ans_count = 0
    ans_value = 0
    # print('T', T)
    check = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            # print('123')
            dfs(i, j, matrix[i][j], 1, -1, -1)
    # print(ans_count, ans_value)
    print('#{} {} {}'.format(T, ans_value - ans_count + 1, ans_count))