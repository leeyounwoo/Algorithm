import sys

sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    num = int(input())
    arr = list(map(int, input().split()))

    result = []
    min_num = arr[0]
    for i in range(num):
        if arr[i] < min_num:
            min_num = arr[i]
            print(min_num)
    result.append(min_num)



