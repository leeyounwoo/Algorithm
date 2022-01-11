import sys
sys.stdin = open('input.txt')

# B리스트에 있는 걸 하나씩 뽑아서 arr(A)와 비교
def binary_search(arr, left, right, target):
    global flag
    # arr.sort()

    start = left
    end = right
    # 왼쪽이 오른쪽보다 왼쪽에 있을 때만 통과
    if left > right:
        return 0

    mid = (left + right) // 2
    if target >= arr[mid] :
        if arr[mid] == target: # 같다면 true
            return 1
        if flag == 'right':
            return 0
        flag = 'right' # 아니면/ target이 더 크다면 flag
        start = mid + 1 # left 한칸 전진

    elif arr[mid] > target:
        if flag == 'left':
            return 0
        flag = 'left'
        end = mid -1

    return binary_search(arr, start, end, target)

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))

    cnt = 0
    for i in B:
        flag = 0
        if binary_search(A, 0, N-1, i):
            cnt += 1
    print('#{} {}'.format(tc, cnt))
