import sys
# input.txt 파일에서 입력값 불러오는 코드
sys.stdin = open('input.txt')
T = int(input())

for Tc in range(1, T + 1):
    canvas = [[0] * 10 for _ in range(10)]  # 캔버스 생성! # 캔버스에 물감 초기화 ( 0 : 흰색,1: 빨강, 2: 파랑, 3: 보라 )
    result = 0 # 결과 담을 공간
    N = int(input())  #몇개 색칠할지 영역의 개수 입력

    for i in range(N):  # input값 2 2 4 4 1  2x2 부터 4x4 색깔 1 빨강으로 칠한다.
                        #  1 2 3 3 1

        r1, c1, r2, c2, color = map(int, input().split())

        for r in range(r1, r2 + 1):
            for c in range(c1, c2 + 1):
                if color == 1:  # 빨강 색칠
                    if canvas[r][c] == 0:  # 배열내의 흰색을
                        canvas[r][c] = 1    # 빨강으로
                    elif canvas[r][c] == 2:  # 겹치는 파랑을 보라로
                        canvas[r][c] = 3
                        result += 1    # 겹치는 부분 합!
                else:  # 파랑 색칠
                    if canvas[r][c] == 0:  # 배열내의 흰색->파랑으로
                        canvas[r][c] = 2
                    elif canvas[r][c] == 1:  # 겹치는 빨강을 보라로
                        canvas[r][c] = 3
                        result += 1 #겹치는 부분 합!
    print('#{} {}'.format(Tc, result))