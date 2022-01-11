import sys
sys.stdin = open('input.txt')

TC = int(input())

for tc in range(1, TC + 1):
    palette = [[0 for _ in range(10)] for _ in range(10)]
    result = 0
    N = int(input())

    for _ in range(N):
        r1, c1, r2, c2, color = map(int, input().split())

        for i in range(r1, r2 + 1):
            for j in range(c1, c2 + 1):
                palette[i][j] += color
                if palette[i][j] >= 3:
                    result += 1

    print(f"#{tc} {result}")
