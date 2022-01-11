import sys
sys.stdin = open('input.txt')

def binary_search():
    result = 0
    for b in B:
        # 초기값
        side = None
        l = 0
        r = N - 1
        while l <= r:
            m = (l + r) // 2
            if b == A[m]: # 탐색 완료
                result += 1
                break
            elif b < A[m]: # 왼쪽 탐색
                r = m - 1
                current = 'left side'
            elif b > A[m]: # 오른쪽 탐색
                l = m + 1
                current = 'right side'
            if side == current:
                break
            side = current
    return result

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split()))) # 정렬 필수
    B = map(int, input().split())
    print('#{} {}'.format(tc, binary_search()))