import sys
sys.stdin = open('input.txt')
from collections import deque

def merge(left, right):

    result = []
    left = deque(left)
    right = deque(right)
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left.popleft())
        else:
            result.append(right.popleft())

    if len(left) > 0:
        result.extend(left)
    if len(right) > 0:
        result.extend(right)

    return result

def merge_sort(arr):
    global count

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    if left[-1] > right[-1]:
        count += 1

    return merge(left, right)

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    numbers = list(map(int, input().split()))

    # N//2번째 원소, 왼쪽 마지막 원소가 오른쪽 마지막 원소보다 큰 경우의 수
    # 2 2 1 1 3 -> 1 1 2 2 3
    count = 0
    middle = merge_sort(numbers)
    middle = middle[len(middle)//2]

    print('#{} {} {}'.format(tc, middle, count))
