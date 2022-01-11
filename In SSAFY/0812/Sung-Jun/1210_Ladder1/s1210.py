import sys
sys.stdin = open('input.txt')

T = 10

for tc in range(T):
    case_num = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    y_len = len(ladder)
    x_len = len(ladder[0])
    dx = [1, -1, 0]
    dy = [0, 0, -1]
    now_x = 0
    now_y = 0

    for j in range(y_len):
        if ladder[y_len-1][x_len-j-1] == 2:
            now_x = x_len - j - 1
            now_y = y_len - 1
            break

    while True:
        for idx in range(3):
            next_x = now_x + dx[idx]
            next_y = now_y + dy[idx]
            if (0 <= next_x < 100 and 0 <= next_y < 100 and
                    ladder[next_y][next_x] == 1):
                ladder[now_y][now_x] += 1
                now_x = next_x
                now_y = next_y
        if now_y == 0:
            break
    print('#{} {}'.format(tc+1, now_x))
