import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T+1):
    test_case = int(input())
    result = []
    max_num = []

    # 100*100 result 리스트 만들기
    for _ in range(100):
        result.append(list(map(int, input().split())))
        # [[13, 24, 13, 24, 1, ..]]

    # row
    for i in range(100):
        total = 0
        for j in range(100):
            total += result[i][j]
        max_num.append(total)

    # col
    for j in range(100):
        total = 0
        for i in range(100):
            total += result[i][j]
        max_num.append(total)

    # diagonal_1
    for i in range(100):
        total = 0
        for j in range(100):
            if i == j :
                total += result[i][j]
        max_num.append(total)

    # diagonal_2
    for i in range(100):
        total = 0
        for j in range(100):
            if i + j == 99:
                total += result[i][j]
        max_num.append(total)

    # 4개 중 최대값
    max_V = max_num[0]
    for max in max_num:
        if max_V <= max:
            max_V = max

    print('#{} {}'.format(test_case, max_V))