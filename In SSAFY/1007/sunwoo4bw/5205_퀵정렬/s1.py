import sys
sys.stdin = open('input.txt')

def partition(arr, start, end):
    pivot = arr[end]  # 배열의 맨 오른쪽 값으로 피봇 설정
    left = start # 맨 처음
    right = end - 1 # pivot의 앞

    while left < right: # left가 right보다 왼쪽에 있을 때 동안
        # 왼쪽(left)은 피봇보다 "큰 값을 찾을 때까지" 오른쪽 전진
        while arr[left] <= pivot:
            left += 1
            if left > right: # left가 right보다 오른쪽에 있으면 끝
                break

        # 오른쪽(right)은 피봇보다 "작은 값을 찾을 때까지" 왼쪽 전진
        while arr[right] >= pivot:
            right -= 1
            if left > right: # left가 right보다 오른쪽에 있으면 끝
                break

        # 만약, 아직 서로의 위치가 유효하다면 (left < right)
        # 아직 교환할 값이 있다는 뜻이므로 교환!
        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]

    # 피봇의 위치가 완전히 결정되었으므로
    # left 위치의 값과 피봇 위치(end)의 값을 교환
    arr[left], arr[end] = arr[end], arr[left]

    # 결정된 피봇의 위치가 이제 left이므로 반환
    return left

def quick_sort(arr, start, end):
    if start < end:
        pivot = partition(arr, start, end)  # 매 시행마다 left 반환 : pivot = 7
        if end == N//2 +1:
            return
        quick_sort(arr, start, pivot - 1)  # 왼쪽 서브 배열 재귀적으로 시행
        quick_sort(arr, pivot + 1, end)

T = int(input())
for tc in range(1, T +1):
    N = int(input())
    A = list(map(int, input().split()))

    quick_sort(A, 0, len(A) - 1)  # 배열, 시작점, 끝지점
    print(A)
    print('#{} {}'.format(tc, A[N//2]))
'''
10개 중 9개만 맞
'''