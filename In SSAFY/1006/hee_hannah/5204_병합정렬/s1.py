import sys
sys.stdin = open('input.txt')


def merge(left, right):
    global cnt
    if left[-1] > right[-1]:
        cnt += 1

    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    if len(left) > 0:
        result.extend(left)
    if len(right) > 0:
        result.extend(right)
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


t = int(input())
for tc in range(1, t+1):
    print('#{}'.format(tc), end=" ")
    n = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    a = merge_sort(arr)
    print('{} {}'.format(a[n//2], cnt))
