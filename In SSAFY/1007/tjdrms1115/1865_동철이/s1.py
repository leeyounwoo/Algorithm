def permutation(N, chance, column_order, k, total, max_chance):
    global result

    if k == N:
        if result < total:
            result = total
    else:
        if total * max_chance < result:
            return

        for i in range(k, N):
            column_order[i], column_order[k] = column_order[k], column_order[i]
            permutation(N, chance, column_order, k + 1, total * (chance[k][column_order[k]]),
                        max_chance / (max(chance[k])))
            column_order[i], column_order[k] = column_order[k], column_order[i]


T = int(input())

answer = []
for tc in range(1, T + 1):

    N = int(input())

    chance = [list(map(int, input().split())) for _ in range(N)]

    max_chance = 1
    for i in range(N):
        max_chance *= max(chance[i])

    # column_order = list(range(N))
    column_order = []
    for i in range(N):
        temp = -1
        tempidx = -1
        for j in range(N):
            if temp < chance[i][j] and (j not in column_order):
                temp = chance[i][j]
                tempidx = j
        column_order.append(tempidx)

    result = 0
    permutation(N, chance, column_order, 0, 1, max_chance)

    result /= (100 ** N)
    result *= 100
    answer.append(result)

for tc in range(1, T + 1):
    print(f'#{tc} {answer[tc-1]:.6f}')
