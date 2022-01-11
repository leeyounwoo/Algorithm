import sys
sys.stdin = open('input.txt')

# 테스트 케이스 입력
T = int(input())

for tc in range(1, T+1):
    # 초기화 작업 통해 10 * 10 행렬 만들기 ( [0, 0, ... , 0]  [0, 0, ... , 0] ...  [0, 0, ... , 0])
    # arr = [[0] * M] * N 은 사용 불가 기억하기!
    # 초기화( 0: 흰색, 1: 빨강색, 2: 파랑색, 3:보라색)
    color_change = [[0] * 10 for _ in range(10)]
    result = 0
    N = int(input())

    for i in range(N):      # 2 2 4 4 1
        r1, c1, r2, c2, color = map(int, input().split())

        for r in range(r1, r2+1):
            for c in range(c1, c2+1):
                if color == 1:          # r1~r2, c1~c2 빨간색을 색칠한다면..?
                    if color_change[r][c] == 0:      # 색깔이 이미 흰색이면 빨강으로 바뀌어라!
                        color_change[r][c] = 1
                    elif color_change[r][c] == 2:    # 색깔이 이미 파랑색이면 빨강과 만나므로 보라색으로!
                        color_change[r][c] = 3
                        result += 1
                elif color == 2:        # r1~r2, c1~c2 파란색을 색칠한다면..?
                    if color_change[r][c] == 0:      # 색깔이 이미 흰색이라면 파랑으로 바뀌어라!
                        color_change[r][c] = 2
                    elif color_change[r][c] == 1:    # 색깔이 이미 빨강색이라면 파랑과 만나므로 보라색으로!
                        color_change[r][c] = 3
                        result += 1

    print('#{} {}'.format(tc, result))