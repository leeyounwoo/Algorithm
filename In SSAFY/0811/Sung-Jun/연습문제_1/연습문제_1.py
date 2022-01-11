import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    limit = int(input())
    numbers = [list(map(int, input().split())) for _ in range(limit)]

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    new_x = new_y = 0
    total = 0
    for i in range(limit):
        for j in range(limit):
            for idx in range(4):
                new_x = j + dx[idx]
                new_y = i + dy[idx]
                if 0 <= new_x < limit and 0 <= new_y < limit:
                    result = numbers[i][j] - numbers[new_y][new_x]
                    if result > 0:
                        total += result
                    else:
                        total += (result*-1)
    print('#{} {}'.format(tc+1, total))