import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(N)]

    num_max = 0 # 반복적인 비교를 위한 초기값 설정
    for i in range(M):
        for j in range(M):
            num_max += puzzle[i][j]

    for i in range(N - M + 1): # 파리채의 세로 이동범위
        for j in range(N - M + 1): # 파리채의 가로 이동범위
            tmp = 0 # 파리채 안의 모든 요소를 더해주기 위한 임시 변수
            for line in puzzle[i:i+M]: # 파리채의 세로 ex) [[3, 3], [13, 9]]
                for element in line[j:j+M]: # 파리채의 가로 ex) [3, 3]
                    tmp += element
            if tmp > num_max: # 모든 요소를 더한 임시 변수가 초기값보다 크면
                num_max = tmp # 그 임시 변수의 값이 초기값으로

    print(f'#{tc + 1} {num_max}')