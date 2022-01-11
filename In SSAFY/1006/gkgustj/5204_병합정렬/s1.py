from collections import deque
import sys
sys.stdin = open('input.txt')

def merge(left, right):
    global cnt

    left =deque(left)
    right = deque(right)

    if left[-1] > right[-1]:
        cnt += 1

    result = []

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

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


T = int(input())

for t in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))

    cnt = 0
    answer = merge_sort(numbers)

    print('#{} {} {}'.format(t, answer[N//2], cnt))