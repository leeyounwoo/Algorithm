import sys
sys.stdin = open('input.txt')
from itertools import combinations


def get_synergy(N, synergy, combi):
    total = 0
    for i in range(len(combi) - 1):
        for j in range(i + 1, len(combi)):
            total += synergy[combi[i]][combi[j]]
            total += synergy[combi[j]][combi[i]]
    return total


T = int(input())

answer = []
for tc in range(1, T + 1):

    N = int(input())

    synergy = [list(map(int, input().split())) for _ in range(N)]

    food_combi = list(combinations(range(N), N // 2))

    result = 100000000
    for i in range(len(food_combi)):
        combiA_synergy = get_synergy(N, synergy, food_combi[i])
        another_combi = tuple(set(range(N)) - set(food_combi[i]))
        combiB_synergy = get_synergy(N, synergy, another_combi)
        if result > abs(combiA_synergy - combiB_synergy):
            result = abs(combiA_synergy - combiB_synergy)

    answer.append(result)

for tc in range(1, T + 1):
    print(f'#{tc} {answer[tc-1]}')

