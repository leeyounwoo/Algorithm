import sys
sys.stdin = open("input.txt")
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    colors = [list(map(int, input().split())) for _ in range(N)]
    white = [[0] * 10 for _ in range(10)]
    for i in range(N):
        x, y = colors[i][0], colors[i][1] # 왼쪽 위 모서리 인덱스
        z, w = colors[i][2], colors[i][3] # 오른쪽 아래 모서리 인덱스
        for j in range(y, w+1):
            for l in range(x, z+1):
                if colors[i][4] == 1:     # 색상 정보 1=빨강
                    white[l][j] += 1
                else:                     # 색상 정보 2=파랑
                    white[l][j] += 2
    count = 0
    for i in range(10):
        for j in range(10):
            if white[i][j] == 3:          # 색상 정보 3=보라
                count += 1
    print('#{} {}'.format(tc, count))
