import sys
sys.stdin = open('input.txt')


def binary(arr, target):
    global cnt
    left = 0
    right = len(arr) - 1
    flag = 0
    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            cnt += 1
            return
        elif arr[mid] > target:
            if flag == 1:
                return
            right = mid - 1
            flag = 1

        elif arr[mid] < target:
            if flag == 2:
                return
            left = mid + 1
            flag = 2

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    a_list = sorted(list(map(int, input().split())))
    b_list = list(map(int, input().split()))

    cnt = 0
    for num in b_list:
        binary(a_list, num)
    print('#{} {}'.format(tc+1, cnt))
