import sys
sys.stdin = open('input.txt')

arr = list(map(int, input().split()))
n = len(arr)

for i in range(1 << n):
    total = 0
    for j in range(n):
        if i & (1 << j):
            total += arr[j]

    if total == 0:
        print('0이 되는 경우가 있습니다!')
