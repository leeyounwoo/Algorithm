import sys
sys.stdin = open('input.txt')


def merge(left, right):
    global cnt
    result = []
    l_idx = 0
    r_idx = 0

    while l_idx < len(left) and r_idx < len(right):
        if left[l_idx] <= right[r_idx]:
            result.append(left[l_idx])
            l_idx += 1
        else:
            result.append(right[r_idx])
            r_idx += 1

    if l_idx < len(left):
        result.extend(left[l_idx:])
        cnt += 1
    if r_idx < len(right):
        result.extend(right[r_idx:])

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
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0

    print('#{} {} {}'.format(tc, merge_sort(arr)[len(arr)//2], cnt))