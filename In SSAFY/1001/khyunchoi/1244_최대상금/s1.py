from itertools import combinations 
import sys
sys.stdin = open('input.txt')


def dfs(depth):
    global result
    if depth >= N:
        result = max(result, int(''.join(map(str, reward))))
        return

    for i in range(len(combi_list)):
        a, b = combi_list[i][0], combi_list[i][1]
        reward[a], reward[b] = reward[b], reward[a]
        dfs(depth+1)
        reward[a], reward[b] = reward[b], reward[a]


T = int(input())
for tc in range(1, T+1):
    reward, N = input().split()
    reward = list(map(int, reward))
    N = int(N)
    combi_list = list(combinations(range(len(reward)), 2))
    
    problem = False
    if N > len(reward) - 1:
        if (N - len(reward)) % 2 == 0:
            problem = True
        N = len(reward) - 1

    overlap = True
    if len(reward) == len(set(reward)):
        overlap = False

    result = 0
    dfs(0)

    if not overlap and problem:
        tmp_result = list(str(result))
        tmp_result[-2], tmp_result[-1] = tmp_result[-1], tmp_result[-2]
        result = int(''.join(tmp_result))

    print('#{} {}'.format(tc,result))