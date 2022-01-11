import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]

    print('#{}'.format(tc), end=' ')
    # 행방향
    # 2차원 순회
    for i in range(N):
        for j in range(N - M + 1):
            flag = 1
            # 회문 검사
            for k in range(M // 2):
                if arr[i][j + k] != arr[i][j + M - 1 - k]:
                    flag = 0
                    break
                    # 틀리면 빠져나가
                    # 회문이 아니면 튀어나가서 다음 if 로 가서 검사
            if flag == 1:  # 출력
                for k in range(M):
                    print('{}'.format(arr[i][j + k]), end='')
                print()

    # 열방향 -> 열, 행 같으니까 위치만 바꿔주면 돼
    # 2차원 순회
    for i in range(N):
        for j in range(N - M + 1):
            flag = 1
            # 회문 검사
            for k in range(M // 2):
                if arr[j + k][i] != arr[j + M - 1 - k][i]:
                    flag = 0
                    break
            if flag == 1:  # 출력
                for k in range(M):
                    print('{}'.format(arr[j + k][i]), end='')
                print()
