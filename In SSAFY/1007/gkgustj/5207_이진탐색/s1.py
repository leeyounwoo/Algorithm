import sys
sys.stdin = open('input.txt')

def binary_search(arr, target):
    global before

    left = 0
    right = N - 1

    while left <= right:
        middle = (left + right) // 2

        if arr[middle] == target:
            return middle
        elif arr[middle] > target:
            if before == 'left':
                return -1

            right = middle - 1
            before = 'left'
        else:
            if before == 'right':
                return -1

            left = middle + 1
            before = 'right'
    
    return -1


T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A.sort()
    cnt = 0

    for target in B:
        before = ''

        idx = binary_search(A, target)

        if idx != -1:
            cnt += 1

    print('#{} {}'.format(t, cnt))