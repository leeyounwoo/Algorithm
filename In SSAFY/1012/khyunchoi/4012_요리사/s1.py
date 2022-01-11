import sys
sys.stdin = open('input.txt')

from itertools import combinations, permutations


def calculate(arr):
    permues = permutations(arr, 2)

    total = 0
    for permu in permues:
        a = permu[0]
        b = permu[1]
        total += table[a][b]

    return total


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N)]
    combies = list(combinations(range(N), N//2))

    result = float('inf')
    for combi in combies:
        if 0 in combi:
            A_list = list(combi)
            B_list = []
            for i in range(N):
                if i not in A_list:
                    B_list.append(i)

            tmp = abs(calculate(A_list) - calculate(B_list))
            result = min(result, tmp)

    print('#{} {}'.format(tc, result))