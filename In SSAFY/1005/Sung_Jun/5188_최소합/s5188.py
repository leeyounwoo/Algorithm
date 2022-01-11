import sys
sys.stdin = open('input.txt')
'''
0,0 부터 num,num 까지의 경로중 최소합을 구하라는 문제
시작 위치는 0,0 으로 고정 
'''


def min_sum(ny, nx):
    global total, result
    dx = [1, 0]
    dy = [0, 1]

    if result and total > result[0]:
        return

    if nx == num-1 and ny == num-1:
        if not result:
            result.append(total)
            return
        elif result[0] > total:
            result[0] = total
            return

    now_x, now_y = nx, ny
    for idx in range(2):
        ny, nx = now_y + dy[idx], now_x + dx[idx]
        if 0 <= ny < num and 0 <= nx < num:
            total += case[ny][nx]
            min_sum(ny, nx)
            total -= case[ny][nx]


T = int(input())
for tc in range(T):
    num = int(input())
    case = [list(map(int, input().split())) for _ in range(num)]
    result = []
    total = case[0][0]
    min_sum(0, 0)
    print('#{} {}'.format(tc+1, result[0]))
