import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())  # NxN 배열과 MxM의 파리채 생성
    flies = [list(map(int, input().split())) for _ in range(N)]

    result = 0
    # N - M + 1까지만 탐색하면 파리채의 크기때문에 빠짐없이 탐색 가능
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            kill_flies = 0
            #파리채 크기만큼 파리 수 더하기
            for row in range(M):
                for col in range(M):
                    kill_flies += flies[j + col][i + row]
            if kill_flies > result:  #최대한 많은 파리를 잡는값을 결과로 저장하기 위함
                result = kill_flies

    print('#{} {}'.format(tc, result))