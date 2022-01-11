import sys
from collections import deque
sys.stdin = open('input.txt')


def merge(left, right):
    result = []
    left = deque(left)
    right = deque(right)
    # cnt
    global cnt
    if left[-1] > right[-1]:
        cnt += 1
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left.popleft())
        else:
            result.append(right.popleft())
    if len(right) > 0:
        result.extend(right)
    if len(left) > 0:
        result.extend(left)

    return result


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


for T in range(1, 1+int(input())):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    result = merge_sort(arr)
    print('#{} {} {}'.format(T, result[N//2], cnt))