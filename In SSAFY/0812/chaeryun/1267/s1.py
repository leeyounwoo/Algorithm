import sys
sys.stdin = open('input.txt')


for tc in range(10):
    test = int(input())
    N = 100
    ladder = [list(map(int, input().split())) for _ in range(N)] # 100
    y = N-1
    x = ladder[N-1].index(2)
    move = 0
    while y > 0:
        if (move == 0 or move == 1) and x > 0 and ladder[y][x-1]:
            x -= 1
            move = 1
        elif (move == 0 or move == 2) and x < N-1 and ladder[y][x+1]:
            x += 1
            move = 2
        else:
            y -= 1
            move = 0
    print("#{} {}".format(test, x))