import sys
sys.stdin = open('input.txt')

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]


def find(si, sj, ei, ej, N):
    stack = []
    stack.append((si, sj))

    while stack:
        now_i, now_j = stack.pop()
        if not check[now_i][now_j]:
            check[now_i][now_j] = True

            for i in range(4):
                next_i, next_j = now_i + di[i], now_j + dj[i]
                if 0 <= next_i < N and 0 <= next_j < N:
                    if not check[next_i][next_j]:
                        if maze[next_i][next_j] == '2':
                            return 1
                        elif maze[next_i][next_j] == '0':
                            stack.append((next_i, next_j))

    return 0


for T in range(1, 1+int(input())):
    N = int(input())
    maze = [input() for _ in range(N)]
    check = [[False] * N for _ in range(N)]
    flag_s = False
    flag_e = False
    for i in range(N):
        if flag_s and flag_e:
            break
        for j in range(N):
            if maze[i][j] == '3':
                si, sj = i, j
                flag_s = True
                if flag_e:
                    break
            if maze[i][j] == '2':
                ei, ej = i, j
                flag_e = True
                if flag_s:
                    break

    ans = find(si, sj, ei, ej, N)
    print('#{} {}'.format(T, ans))
