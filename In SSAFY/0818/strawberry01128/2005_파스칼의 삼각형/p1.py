def paskal(item):
    for i in range(item):
        table.append([0] * (i + 1))

        for k in range(i + 1):
            if k == 0 or k == i:
                table[i][k] = 1
            else:
                # #table[i][1] = table[i-1][0]+[i-1][1]
                table[i][k] = table[i - 1][k - 1] + table[i - 1][k]
    return table


T = int(input())
for test_case in range(1, T + 1):
    power = int(input())
    table = []
    print('#{}'.format(test_case))
    for _ in (paskal(power)):
        print(*_)
