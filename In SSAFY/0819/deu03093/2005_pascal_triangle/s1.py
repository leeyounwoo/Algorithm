import sys
from pprint import pprint

def pascal(n):
    d = [[1] * n for _ in range(n)]
    for i in range(2, n):
        for j in range(1, i):
            # print(i, j)
            d[i][j] = d[i-1][j-1] + d[i-1][j]
    return d

sys.stdin = open('input.txt')
for T in range(1, 1 + int(input())):
    n = int(input())
    ans = pascal(n)
    print('#{}'.format(T))
    for i in range(n):
        for j in range(0, i+1):
            print(ans[i][j], end=' ')
        print()