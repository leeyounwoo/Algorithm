import sys
# input.txt 파일에서 입력값 불러오는 코드
sys.stdin = open('input.txt')

T = 10
for t in range(T):
    test = int(input())
    N = 100
    ladder = [list(map(int, input().split())) for _ in range(N)]
    dy = N-1
    dx = ladder[N-1].index(2)
    move = 0
    while d_y > 0:
        if (move == 0 or move == 1)
            dx -= 1
            move = 1
        elif (move == 0 or move == 2)
            dx += 1
            move = 2
        else:
            dy -= 1
            move = 0
    print("#{} {}".format(test, dx))