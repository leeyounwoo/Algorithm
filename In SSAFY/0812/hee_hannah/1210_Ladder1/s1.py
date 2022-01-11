import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    n = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]

    y = 99
    for k in range(99, -1, -1):
        if ladder[y][k] == 2:
            x = k
    for y in range(99, -1, -1):
        for x in range(99, -1, -1):
            while True:
                y -= 1
                if x+1 <= 99 and ladder[y][x+1] == 1: #우
                    x += 1
                elif x-1 >= 0 and ladder[y][x-1] == 1: #좌
                    x -= 1
                elif y-1 >= 0 and ladder[y-1][x] == 1: #위
                    y -= 1

                if y == 0:
                    break
                print(x)



