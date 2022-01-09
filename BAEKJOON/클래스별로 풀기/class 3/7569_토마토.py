import sys
from collections import deque


dh, di, dj =[0, 0, 0, 0, 1, -1], [1, -1, 0, 0, 0, 0], [0, 0, 1, -1, 0, 0]
def input():
    return sys.stdin.readline().rstrip()


def bfs_for(total, done_cnt, len_h, len_i, len_j, now_done_list):
    ans = 0
    now_list = deque(now_done_list)
    while True:
        if not now_list:
            return -1
        if total == done_cnt:
            return ans
        next_list = deque()
        ans += 1
        for now_h, now_i, now_j in now_list:
            for k in range(6):
                next_h, next_i, next_j = now_h + dh[k], now_i + di[k], now_j + dj[k]
                if 0 <= next_h < len_h and 0 <= next_i < len_i and 0 <= next_j < len_j:
                    if tomatos[next_h][next_i][next_j] == 0:
                        tomatos[next_h][next_i][next_j] = 1
                        next_list.append((next_h, next_i, next_j))
                        done_cnt += 1
        now_list = next_list


sys.stdin = open('input.txt')
len_j, len_i, len_h = map(int, input().split())

total = len_h * len_i * len_j
done_cnt = 0
now_done_list = []
tomatos = []
for h in range(len_h):
    temp_h = []
    for i in range(len_i):
        temp = list(map(int, input().split()))
        temp_h.append(temp)
        for j in range(len_j):
            if temp[j] == 1:
                done_cnt += 1
                now_done_list.append([h, i, j])
            elif temp[j] == -1:
                total -= 1
    tomatos.append(temp_h)

ans = bfs_for(total, done_cnt, len_h, len_i, len_j, now_done_list)
print(ans)
