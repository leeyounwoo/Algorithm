import sys

sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T + 1):
    N = int(input())
    result = [[0] * 10 for _ in range(10)]

    for n in range(N):
        r1, c1, r2, c2, color = map(int, input().split())

        for i in range(r1, r2 + 1):
            for j in range(c1, c2 + 1):
                if result[i][j] == color:
                    continue
                result[i][j] += color

    cnt = 0
    for x in range(len(result)):
        for y in range(len(result[x])):
            if result[x][y] >= 3:
                cnt += 1

    print(f'#{t} {cnt}')