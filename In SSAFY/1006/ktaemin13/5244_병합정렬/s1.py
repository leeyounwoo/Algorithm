import sys
sys.stdin = open('input.txt')


'''
Merge Sort
- 평균 시간 복잡도: O(nlogn)
- 특징: 안정 정렬
'''


def merge(left, right):
    global cnt

    left_N, right_N = len(left), len(right)
    result = [0] * (left_N + right_N)
    left_i, right_i = 0, 0
    i = 0

    if left[-1] > right[-1]:
        cnt += 1

    while left_i != left_N and right_i != right_N:
        if left[left_i] <= right[right_i]:
            result[i] += left[left_i]
            i += 1
            left_i += 1
        else:
            result[i] += right[right_i]
            i += 1
            right_i += 1

    if left_i != left_N:
        while left_i != left_N:
            result[i] += left[left_i]
            i += 1
            left_i += 1

    if right_i != right_N:
        while right_i != right_N:
            result[i] += right[right_i]
            i += 1
            right_i += 1

    return result

    # ex)
    # result: [1, 3]
    # left: []
    # right: [4, 5]


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    Data = list(map(int, input().split()))
    cnt = 0
    Data = merge_sort(Data)

    print('#{} {} {}'.format(tc, Data[N//2], cnt))


