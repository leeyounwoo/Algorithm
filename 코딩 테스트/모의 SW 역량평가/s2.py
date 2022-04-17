from itertools import combinations
import sys
from pprint import pprint
sys.stdin = open('input.txt')


def get_neighboor(i, j, max_i, max_j):
    list = []
    if i-1 >= 0:
        list.append([i-1, j])
    if j+1 < max_j:
        list.append([i, j+1])
    if i+1 < max_i and j+1 < max_j:
        list.append([i+1, j+1])
    if i+1 < max_i:
        list.append([i+1, j])
    if i+1 < max_i and j-1 >= 0:
        list.append([i+1, j-1])
    if j-1 >= 0:
        list.append([i, j-1])
    return list



for T in range(1, 1+int(input())):
    MAX_J, MAX_I = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(MAX_I)]
    center = []
    for i in range(MAX_I):
        for j in range(MAX_J):
            center.append([i, j])
    dictionary = {i: {j: [] for j in range(MAX_J)} for i in range(MAX_I)}
    for i in range(MAX_I):
        for j in range(MAX_J):
            dictionary[i][j] = get_neighboor(i, j, MAX_I, MAX_J)

    ans = 0
    for temp in combinations(center, 4):
        flag_cnt = 0
        for i in range(4):
            cnt = 0
            for j in range(4):
                # 하나라도 겹치는게 있음
                if i != j and temp[j] in dictionary[temp[i][0]][temp[i][1]]:
                    cnt += 1
            # 하나도 겹치는게 없음
            if cnt == 0:
                break
            elif flag_cnt < cnt:
                flag_cnt = cnt
        else:
            if flag_cnt >= 2:
                flag = 0
                for i in range(4):
                    flag += graph[temp[i][0]][temp[i][1]]
                flag2 = flag ** 2
                if flag2 > ans:
                    ans = flag2
    print('#{} {}'.format(T, ans))




