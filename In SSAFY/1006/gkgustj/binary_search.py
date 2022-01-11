'''
이진탐색
- 반드시 배열이 정렬되어있어야 함
'''

def binary_search(arr, target):
    arr.sort()

    left = 0
    right = len(arr) - 1

    while left <= right:
        middle = (left + right) // 2

        if arr[middle] == target:
            return middle
        elif arr[middle] > target:
            right = middle - 1
        else:
            left = middle + 1
    
    # 배열에서 찾는 값이 없을 경우
    return -1


arr = [5, 3, 7, 6, 2, 1, 4]
target = 3

print(binary_search(arr, target))