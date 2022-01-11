import sys
sys.stdin = open('input.txt')

def binary_search(arr, target):
    arr.sort()
    a = len(arr)
    left = 0
    right = len(arr) - 1
    mid = (left + right) // 2
    s = (arr[0]+arr[mid])//2
    e = (arr[right]+arr[mid])//2

    if target in arr:
        if s <= target <= e:
            return 1
        elif a == 3:
            return 1
    return 0

t = int(input())
for tc in range(1, t+1):
    print('#{}'.format(tc), end=" ")
    a, b = map(int, input().split())
    a_arr = list(map(int, input().split()))
    b_arr = list(map(int, input().split()))
    cnt = 0
    for i in b_arr:
        cnt += binary_search(a_arr, i)
    print(cnt)


#
# def binary_search(arr, target):
#     arr.sort()
#
#     left = 0
#     right = len(arr) - 1
#
#     while left <= right:
#         mid = (left + right) // 2
#
#         if arr[mid] == target:
#             return 1
#         elif arr[mid] > target:
#             right = mid - 1
#         elif arr[mid] < target:
#             left = mid + 1
#
#     return 0
