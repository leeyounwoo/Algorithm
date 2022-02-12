import sys
from copy import deepcopy

def input():
    return sys.stdin.readline().rstrip()


def functionA(n, m):
    new_array = [[0] * m for _ in range(n)]
    cnt = min(n, m) // 2

    for c in range(cnt):
        for i in range(c, n-c):
            if i == c:
                for j in range(c, m-c):
                    if j == m - c - 1:
                        new_array[i][j] = array[i+1][j]
                    else:
                        new_array[i][j] = array[i][j+1]
            elif i == n - c - 1:
                for j in range(c, m - c):
                    if j == c:
                        new_array[i][j] = array[i-1][j]
                    else:
                        new_array[i][j] = array[i][j-1]
            else:
                new_array[i][c] = array[i-1][c]
                new_array[i][m-c-1] = array[i+1][m-c-1]
    return new_array

sys.stdin = open('input.txt')
n, m, r = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]
for i in range(r):
    array = functionA(n, m)
for i in range(n):
    for j in range(m):
        print(array[i][j], end=" ")
    print()