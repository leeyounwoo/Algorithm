import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    Ci = list(map(int, input().split()))
    idx_Ci = []
    for idx in range(1, M+1):
        idx_Ci.append([Ci[idx-1], idx])
    queue = []

    while len(queue) < N:
        queue.append(idx_Ci.pop(0))

    while len(queue) != 1:
        tmp_pizza = queue.pop(0)
        tmp_pizza[0] = tmp_pizza[0]//2

        if tmp_pizza[0]:
            queue.append(tmp_pizza)
        else:
            if idx_Ci:
                queue.append(idx_Ci.pop(0))

    result = queue.pop()[1]
    print('#{} {}'.format(tc, result))