import sys
sys.stdin = open('input.txt')

t = int(input())

for tc in range(1, t+1):

    n = int(input())
    arr = [[0] * 10 for i in range(10)]
    result = 0
    for _ in range(n):
        x1, y1, x2, y2, color = map(int, input().split())

        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                arr[i][j] += color

                if arr[i][j] == 3:
                    result += 1

    print('#{0} {1}'.format(tc, result))