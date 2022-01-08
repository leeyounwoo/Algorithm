import sys
from collections import deque


di, dj = [1, -1, 0, 0], [0, 0, 1, -1]
def input():
    return sys.stdin.readline().rstrip()


def bfs_for(total, done_cnt, len_i, len_j, now_done_list):
    ans = 0
    now_list = deque(now_done_list)
    while True:
        if not now_list:
            return -1
        if total == done_cnt:
            return ans
        next_list = deque()
        ans += 1
        for now_i, now_j in now_list:
            for k in range(4):
                next_i, next_j = now_i + di[k], now_j + dj[k]
                if 0 <= next_i < len_i and 0 <= next_j < len_j and tomatos[next_i][next_j] == 0:
                    tomatos[next_i][next_j] = 1
                    next_list.append((next_i, next_j))
                    done_cnt += 1
        now_list = next_list


sys.stdin = open('input.txt')
len_j, len_i = map(int, input().split())

total = 0
done_cnt = 0
now_done_list = []
tomatos = []
for i in range(len_i):
    temp = list(map(int, input().split()))
    not_tomato_cnt = 0
    for j in range(len_j):
        if temp[j] == 1:
            done_cnt += 1
            now_done_list.append([i, j])
        elif temp[j] == -1:
            not_tomato_cnt += 1
    total += len_j - not_tomato_cnt
    tomatos.append(temp)

# ans = 0
ans = bfs_for(total, done_cnt, len_i, len_j, now_done_list)
print(ans)

