import sys

sys.stdin = open("input.txt")



T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    numbers = [list(map(int, input().split())) for _ in range(N)]
    result = []
    checked = [0] * N
    for i in range(N):
        row = []
        min_row = 10
        for j in range(N):
            row.append(numbers[i][j])
        for m in range(N):
            if checked[m] == 0:
               if row[m] < min_row:
                   min_row = row[m]
                   checked[m] = 1
            else:
                pass
        result.append(min_row)
    print(result)
