import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    result = []
    arr = []
    for i in range(N):
        arr.append(input())

    # 가로 검색
    for r in range(N):
        for c in range(N-M+1):
            if arr[r][c:c+M] == arr[r][c:c+M][::-1]:
                result.append(arr[r][c:c+M])

    # 세로 검색
    for r in range(N - M + 1):
        for c in range(N):
            c_list = []                             # 새로 열 리스트를 만들어주기
            for i in range(M):
                c_list.append(arr[r+i][c])
            if c_list == c_list[ : : -1]:           # 세로줄이 회문이면
                    result.append(''.join(c_list))  # 결과리스트에 추가.


    print('#{} {}'.format(tc, result[0]))


