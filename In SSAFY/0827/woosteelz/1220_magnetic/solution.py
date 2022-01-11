import sys
sys.stdin = open('input.txt')

for tc in range(1):
    num = int(input())
    temp = [list(map(int, input().split())) for _ in range(100)]
    table = list(map(list, zip(*temp)))

    for i in range(100):
        for j in range(100):
            if table[i][j] == 1:
                table[i][j] = 0
            elif table[i][j] == 2:
                break
        for j in range(99, -1, -1):
            if table[i][j] == 2:
                table[i][j] = 0
            elif table[i][j] == 1:
                break

    for a in table:
        print(*a)
