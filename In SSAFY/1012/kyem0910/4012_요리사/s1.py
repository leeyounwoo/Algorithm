import sys
sys.stdin = open('input.txt')
from itertools import combinations

def decide_arr():
    temp = [i for i in range(N)]
    combis = list(combinations(temp, int(N/2)))
    for combi in combis:
        cook(combi)

def cook(arr):
    global result
    case1 = list(arr)
    case2 = []
    for i in range(N):
        if i not in case1:
            case2.append(i)

    case1_synergy = 0
    case2_synergy = 0
    for i in range(int(N/2)):
        for j in range(i+1, int(N/2)):
            a = case1[i]
            b = case1[j]
            c = case2[i]
            d = case2[j]
            case1_synergy += info[a][b] + info[b][a]
            case2_synergy += info[c][d] + info[d][c]

    if result > abs(case1_synergy - case2_synergy):
        result = abs(case1_synergy - case2_synergy)

T = int(input())
for tc in range(T):
    N = int(input())
    info = [list(map(int, input().split())) for _ in range(N)]
    result = 10000000
    decide_arr()
    print('#{} {}'.format(tc+1, result))