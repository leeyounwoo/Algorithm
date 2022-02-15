import sys

def input():
    return sys.stdin.readline().rstrip()


sys.stdin = open('input.txt')
n, m = map(int, input().split())
array1 = [list(map(int, input().split())) for _ in range(n)]
m, k = map(int, input().split())
array2 = [list(map(int, input().split())) for _ in range(m)]

array = [[0] * k for _ in range(n)]
for i in range(n):
    for j in range(k):
        temp = 0
        for i_1 in range(m):
            temp += array1[i][i_1] * array2[i_1][j]
        array[i][j] = temp

for i in range(n):
    for j in range(k):
        print(array[i][j], end=" ")
    print()