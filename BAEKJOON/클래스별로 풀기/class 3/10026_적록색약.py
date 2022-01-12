import sys
from collections import deque

di, dj = [1, -1, 0, 0], [0, 0, 1, -1]
def input():
    return sys.stdin.readline().rstrip()


def all(check, n):
    for i in range(n):
        for j in range(n):
            if not check[i][j]:
                return [i, j]

    return True


def bfs_rg(n):
    cnt = 1
    check = [[0] * n for _ in range(n)]

    while True:
        temp = all(check, n)
        if temp == True:
            break

        else:
            if graph[temp[0]][temp[1]] == 'R':
                flag = 1
            elif graph[temp[0]][temp[1]] == 'G':
                flag = 1
            elif graph[temp[0]][temp[1]] == 'B':
                flag = 3
            q = deque([[temp[0], temp[1], flag]])

            check[temp[0]][temp[1]] = cnt
            while q:
                now_i, now_j, now_flag = q.popleft()
                for k in range(4):
                    next_i, next_j = now_i + di[k], now_j + dj[k]
                    if 0 <= next_i < n and 0 <= next_j < n and check[next_i][next_j] == 0:
                        if graph[next_i][next_j] == 'R':
                            next_flag = 1
                        elif graph[next_i][next_j] == 'G':
                            next_flag = 1
                        elif graph[next_i][next_j] == 'B':
                            next_flag = 3
                        if next_flag == now_flag:
                            check[next_i][next_j] = cnt
                            q.append([next_i, next_j, next_flag])
            cnt += 1

    return cnt

def bfs_normal(n):
    cnt = 1
    check = [[0] * n for _ in range(n)]

    while True:
        temp = all(check, n)
        if temp == True:
            break

        else:
            if graph[temp[0]][temp[1]] == 'R':
                flag = 1
            elif graph[temp[0]][temp[1]] == 'G':
                flag = 2
            elif graph[temp[0]][temp[1]] == 'B':
                flag = 3
            q = deque([[temp[0], temp[1], flag]])

            check[temp[0]][temp[1]] = cnt
            while q:
                now_i, now_j, now_flag = q.popleft()
                for k in range(4):
                    next_i, next_j = now_i + di[k], now_j + dj[k]
                    if 0 <= next_i < n and 0 <= next_j < n and check[next_i][next_j] == 0:
                        if graph[next_i][next_j] == 'R':
                            next_flag = 1
                        elif graph[next_i][next_j] == 'G':
                            next_flag = 2
                        elif graph[next_i][next_j] == 'B':
                            next_flag = 3
                        if next_flag == now_flag:
                            check[next_i][next_j] = cnt
                            q.append([next_i, next_j, next_flag])
            cnt += 1

    return cnt


sys.stdin = open('input.txt')
n = int(input())
graph = [list(input()) for _ in range(n)]

check_normal = [[0] * n for _ in range(n)]
check_rg = [[0] * n for _ in range(n)]

ans_normal = bfs_normal(n) - 1
ans_rg = bfs_rg(n) - 1

print('{} {}'.format(ans_normal, ans_rg))