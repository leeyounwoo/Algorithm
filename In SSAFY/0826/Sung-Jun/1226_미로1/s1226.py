import sys
sys.stdin = open('input.txt')


T = 10
for _ in range(T):
    tc = int(input())
    box = [input() for _ in range(16)]
    visited = [[0] * 16 for _ in range(16)]
    dyx = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    start = None
    for i in range(16):
        flag = 0
        for j in range(16):
            if box[i][j] == '2':
                start = (i, j)
                flag = 1
                break
        if flag:
            break

    flag = 0
    result = 0
    stack = [start]
    while stack:
        nx = stack.pop()
        if visited[nx[0]][nx[1]] == 0:
            visited[nx[0]][nx[1]] += 1
            for dy, dx in dyx:
                n_i = nx[0] + dy
                n_j = nx[1] + dx
                if 0 <= n_i < 16 and 0 <= n_j < 16:
                    if visited[n_i][n_j] == 0 and box[n_i][n_j] == '0':
                        stack.append((n_i, n_j))
                if box[n_i][n_j] == '3':
                    result = 1
                    flag = 1
                    break
            if flag:
                break
    print('#{} {}'.format(tc, result))

