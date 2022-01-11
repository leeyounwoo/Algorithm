import sys
sys.stdin = open('input.txt')

for _ in range(10):
    T = int(input())
    matrix = []
    result = []

    for _ in range(100):
        lst = list(map(int, input().split()))
        matrix.append(lst)
        result.append(sum(lst))

    for col in range(100):
        col_total = 0
        for row in range(100):
            col_total += matrix[row][col]
        result.append(col_total)

    diagonal_total1 = 0
    diagonal_total2 = 0
    for i in range(100):
        diagonal_total1 += matrix[i][i]
        diagonal_total2 += matrix[i][99 - i]
    result.extend([diagonal_total1, diagonal_total2])

    print('#{0} {1}'.format(T, max(result)))