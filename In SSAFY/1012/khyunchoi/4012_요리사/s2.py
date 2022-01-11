import sys
sys.stdin = open('input2.txt')


def get_combi(arr, idx):
    if len(arr) == N//2:
        diy_combies.append(arr)
        return

    for i in range(idx, N):
        if not visited[i]:
            visited[i] = 1
            get_combi(arr+[my_list[i]], i)
            visited[i] = 0


def get_permu(arr, diy_permues):
    if len(arr) == 2:
        diy_permues.append(arr)
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            get_permu(arr+[my_list[i]], diy_permues)
            visited[i] = 0


def calculate(arr):
    diy_permues = []
    get_permu([], diy_permues)

    total = 0
    for permu in diy_permues:
        a = permu[0]
        b = permu[1]
        total += table[a][b]

    return total


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N)]

    my_list = list(range(N))
    visited = [0] * N

    diy_combies = []
    get_combi([], 0)

    result = float('inf')
    for combi in diy_combies:
        if 0 in combi:
            A_list = combi
            B_list = []
            for i in range(N):
                if i not in A_list:
                    B_list.append(i)

            tmp = abs(calculate(A_list) - calculate(B_list))
            result = min(result, tmp)
    print(diy_combies)
    print('#{} {}'.format(tc, result))