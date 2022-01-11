import sys
sys.stdin = open('input.txt')
from pprint import pprint

base_station = {'A': 1, 'B': 2, 'C': 3}
di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]
for T in range(1, 1+int(input())):
    N = int(input())
    arr_map = [list(input()) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            # A, B, C에 들어있는지
            if arr_map[i][j] in base_station:
                now = arr_map[i][j]
                # A는 1, B는 2, C는 3만큼 반복
                max_distance = base_station[now]
                for d in range(1, 1+max_distance):
                    for k in range(4):
                        next_i, next_j = i + (di[k] * d), j + dj[k] * d
                        if 0 <= next_i < N and 0 <= next_j < N and arr_map[next_i][next_j] == 'H':
                            arr_map[next_i][next_j] = 'X'
    ans = 0
    for i in arr_map:
        for j in i:
            if j == 'H':
                ans += 1
    print('#{} {}'.format(T, ans))
