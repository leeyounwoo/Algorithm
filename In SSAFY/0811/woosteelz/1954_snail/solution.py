import sys
sys.stdin = open('input.txt')

TC = int(input())
for tc in range(TC):
    num = int(input())
    visited = [[False for _ in range(num)] for _ in range(num)]
    ans = [[0 for _ in range(num)] for _ in range(num)]
    dir_x = [0, 1, 0, -1]
    dir_y = [1, 0, -1, 0]
    # ans값 업데이트용
    curr_x, curr_y = 0, 0
    # 방향전환용
    i = 0

    ans[0][0] = 1
    visited[0][0] = True

    for _ in range(num ** 2 - 1):
        next_x = curr_x + dir_x[i]
        next_y = curr_y + dir_y[i]
        if 0 <= next_x < num and 0 <= next_y < num and not visited[next_x][next_y]:
            pass
        else:
            i = (i + 1) % 4
            next_x = curr_x + dir_x[i]
            next_y = curr_y + dir_y[i]
        ans[next_x][next_y] = ans[curr_x][curr_y] + 1
        visited[next_x][next_y] = True
        curr_x = next_x
        curr_y = next_y

    print('#{}'.format(tc+1))
    for a in ans:
        print(*a)

