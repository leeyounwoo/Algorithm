import sys
sys.stdin = open('input.txt')

def partition(arr, start, end):
    pivot = (start+end) // 2 # 배열의 가운데로 피봇 설정

    while start < end: # start가 end보다 왼쪽에 있을 때 동안

        # 왼쪽(start) : 오른쪽 전진
        # i) start가 피봇보다 "큰 값"이기 전까지 - 작을 동안~
        # ii) start가 end보다 왼쪽에 있을 동안~
        while arr[start] < arr[pivot] and start < end:
            start += 1

        # 오른쪽(end) : 왼쪽 전진
        # i) end가 피봇보다 "작은 값"이기 전까지 - 클 동안~
        # ii) start가 end보다 왼쪽에 있을 동안~
        while arr[end] >= arr[pivot] and start < end:
            end -= 1

        # 만약, 아직 서로의 위치가 유효하다면 (start < end)
        # 아직 교환할 값이 있다는 뜻이므로 교환! start <-> end
        if start <= end:
            if start == pivot : # start<->end하기 전에 start랑 pivot이랑 같다면
                pivot = end     # pivot = end
            arr[start], arr[end] = arr[end], arr[start]

    # 피봇의 위치가 완전히 결정되었으므로
    # left 위치의 값과 피봇 위치(end)의 값을 교환
    arr[pivot], arr[end] = arr[end], arr[pivot]   # 처음 while 돌고 여기로 와야겠네! start = end니까

    # 결정된 피봇의 위치가 이제 end이므로 end 반환
    return end

def quick_sort(arr, start, end):
    if start < end:
        pivot = partition(arr, start, end)  # 매 시행마다 end
        quick_sort(arr, start, pivot - 1)  # 피봇보다 작은
        quick_sort(arr, pivot + 1, end) # 피봇보다 큰

T = int(input())
for tc in range(1, T +1):
    N = int(input())
    A = list(map(int, input().split()))

    quick_sort(A, 0, len(A) - 1)  # 배열, 시작점, 끝지점
    # print(A)
    print('#{} {}'.format(tc, A[N//2]))