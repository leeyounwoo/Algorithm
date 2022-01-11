def merge(left, right):
    global cnt
    result = []

    while len(left) and len(right):
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    if len(left):
        result.extend(left)
        cnt += 1
    if len(right):
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


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0

    print('#{} {} {}'.format(tc, merge_sort(arr)[len(arr)//2], cnt))