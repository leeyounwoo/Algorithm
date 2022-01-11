'''
Merge Sort
- 평균 시간 복잡도: O(nlogn)
- 특징: 안정 정렬
'''

def merge(left, right):
    # left: [1]
    # right: [3, 4, 5]
    result = []

    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    # ex)
    # result: [1]
    # left: []
    # right: [3, 4, 5]

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


arr = [5, 3, 7, 6, 2, 1, 4]
print(merge_sort(arr))