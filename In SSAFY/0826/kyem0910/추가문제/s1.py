import sys
sys.stdin = open("input.txt")

def check(i, j, cover):
    for k in range(1, cover+1):
        if arr[i+k][j] == 'H' and i+k < n:
            arr[i+k][j] = 'X'
        if arr[i-k][j] == 'H' and i-k >= 0:
            arr[i-k][j] = 'X'
        if arr[i][j+k] == 'H' and j+k < n:
            arr[i][j+k] = 'X'
        if arr[i][j-k] == 'H' and j-k >= 0:
            arr[i][j-k] = 'X'

T = int(input())
for tc in range(T):
    n = int(input())
    arr = [list(input()) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 'A':
                check(i, j, 1)
            elif arr[i][j] == 'B':
                check(i, j, 2)
            elif arr[i][j] == 'C':
                check(i, j, 3)
    result = 0
    for row in arr:
        result += row.count('H')
    print("#{} {}".format(tc+1, result))