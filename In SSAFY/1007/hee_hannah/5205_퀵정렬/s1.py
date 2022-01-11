import sys
sys.stdin = open('input.txt')


def partition(arr, start, end):
    pivot = (start + end) // 2 # 중간 지점

    while start < end:
        # 왼쪽(left)은 피봇보다 "큰 값을 찾을 때까지" 오른쪽 전진
        while arr[start] < arr[pivot] and start < end:
            start += 1

        # 오른쪽(right)은 피봇보다 "작은 값을 찾을 때까지" 왼쪽 전진
        while arr[end] >= arr[pivot] and start < end:
            end -= 1

        # 만약, 아직 서로의 위치가 유효하다면 (start < end)
        # 아직 교환할 값이 있다는 뜻이므로 교환!
        if start <= end:
            if start == pivot:
                pivot = end
            arr[start], arr[end] = arr[end], arr[start]

    # 피봇의 위치가 완전히 결정되었으므로
    # left 위치의 값과 피봇 위치(end)의 값을 교환
    arr[pivot], arr[end] = arr[end], arr[pivot]

    return end # 피봇 위치 반환

def quick_sort(arr, start, end):
    if start < end:
        pivot = partition(arr, start, end) # 피봇 위치 반환
        quick_sort(arr, start, pivot - 1)  # 왼쪽 서브 배열 재귀적으로 시행
        quick_sort(arr, pivot + 1, end) # 오른쪽 서브 배열 재귀적으로 시행

t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    arr = list(map(int, input().split()))

    quick_sort(arr, 0, n - 1)  # 배열, 시작점, 끝지점
    print('#{} {}'.format(tc, arr[n//2]))


# 런타임에러!
#
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#
#     pivot = arr[len(arr) // 2]
#     less = []
#     equal = []
#     more = []
#
#     for num in arr:
#         if num < pivot:
#             less.append(num)
#         elif num == pivot:
#             equal.append(num)
#         else:
#             more.append(num)
#
#     return quick_sort(less) + equal + quick_sort(more)
#
#
# t = int(input())
# for tc in range(1, t+1):
#     print('#{}'.format(tc), end=" ")
#     n = int(input())
#     arr = list(map(int, input().split()))
#     print(quick_sort(arr)[n//2])
