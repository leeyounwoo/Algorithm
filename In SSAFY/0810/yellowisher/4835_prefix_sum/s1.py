import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(T):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    max_num = min_num = 0
    for j in range(M):
        max_num += arr[j]
        min_num += arr[j]

    for i in range(0, N-M+1):
        sum_num1 = 0
        for j in range(M):
            sum_num1 += arr[i+j]
        if sum_num1 > max_num:
            max_num = sum_num1

    for i in range(0, N-M+1):
        sum_num2 = 0
        for j in range(M):
            sum_num2 += arr[i+j]
        if sum_num2 < min_num:
            min_num = sum_num2

    print("#%d %d"%(test_case + 1, max_num - min_num))