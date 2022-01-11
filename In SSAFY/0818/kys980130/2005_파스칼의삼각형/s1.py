import sys
sys.stdin = open("input.txt")
T = int(input())
for tc in range(T):
    n = int(input())
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i+1):
            if j == 0 or j == i:
                result[i][j] = 1
            else:
                result[i][j] = result[i-1][j-1]+result[i-1][j]
    print('#{}'.format(tc+1))
    for i in range(n):
        for j in range(n):
            if result[i][j] == 0:
                print('', end="")
            else:
                print(result[i][j], end=" ")
        print()
