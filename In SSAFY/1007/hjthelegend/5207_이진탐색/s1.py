import sys
sys.stdin = open('input.txt')

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    flag = 0

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return True

        elif arr[mid] > target:
            right = mid - 1
            if flag == 2:
                return False
            flag = 2

        elif arr[mid] < target:
            left = mid + 1
            if flag == 1:
                return False
            flag = 1

    return False

t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    count = 0
    for i in B:
        if binary_search(A, i):
            count += 1
    print('#{} {}'.format(tc, count))
