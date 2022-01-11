import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    N = int(input())
    red = []
    blue = []

    for _ in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        for i in range(r1, r2+1):
            for j in range(c1, c2+1):
                if color == 1:
                    red.append((i, j))
                else:
                    blue.append((i, j))
    count = 0
    for i in range(len(red)):
        for j in range(len(blue)):
            if red[i][0] == blue[j][0] and red[i][1] == blue[j][1]:
                count += 1

    print('#{} {}'.format(tc + 1, count))
