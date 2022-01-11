'''
이진탐색
- 반드시 배열이 정렬되어있어야 함
'''

import sys
sys.stdin = open('input.txt')


def binary_search(arr, target):
    arr.sort()  # 오름차순 정렬

    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1

    # 만약 배열에서 찾는 값이 없을 경우
    # -1 리턴 (혹은 문제에서 시키는 대로)
    return -1


T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))  # 정렬 필수!!
    B = map(int, input().split())
    print('#{} {}'.format(test_case, binary_search(A, B)))
