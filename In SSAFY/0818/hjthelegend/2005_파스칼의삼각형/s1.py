import sys
sys.stdin = open('input.txt')

t = int(input())

for tc in range(1, t+1):
    n = int(input())

    arr = []
    for i in range(n):
        arr.append([])
        arr[i].append(1)

        for j in range(1, i):
            arr[i].append(arr[i-1][j-1] + arr[i-1][j])

        if n != 0:
            arr[i].append(1)

    for i in arr:
        print(*i)