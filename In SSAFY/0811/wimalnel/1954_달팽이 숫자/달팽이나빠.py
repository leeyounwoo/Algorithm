import sys
# input.txt 파일에서 입력값 불러오는 코드
sys.stdin = open('input.txt')
T = int(input())

for test_case in range(1, 1 + T):
    print('#{}'.format(test_case))

    N = int(input())  # N은 1이상 10이하 정수

    Snail = [[0] * N for _ in range(N)] # N행 M열 배열 만들기!! << 익숙해지자 자주쓰는 코드 / 여기선N행N열
    dx = [0, 1, 0, -1]  # 하, 상  //행
    dy = [1, 0, -1, 0]  # 우, 좌  //열
                        # 오른쪽 = 0, 아래=1, 왼쪽= 2, 위=3


    x = 0  # 초기 값 0,0
    y = 0
    way = 0  # 초기 방향 설정 오른쪽

    for i in range(1, N*N + 1):  ## 배열의 크기는 N x N 이다.
        Snail[x][y] = i
        # Snail이 [0][0]위치에  숫자 1부터 쭉~
        # 배열의 크기를 넘어가지 않으려는 노력
        if 0<=x+dx[way]<N and 0<=y+dy[way]<N and Snail[x+dx[way]][y+dy[way]] == 0:

            x += dx[way]
            y += dy[way]
            # 나쁜 달팽이가 벽에 부딛히면 좌절합니다.

        else:
            if way == 3:  # 0 1 2 3 반복을 위해 012301230123~~
                way = 0
            else:
                way += 1  # way가 하나씩 증가하면서
            x += dx[way]
            y += dy[way]

    for i in range (N) :
        print(*Snail[i])  # *로 언팩킹