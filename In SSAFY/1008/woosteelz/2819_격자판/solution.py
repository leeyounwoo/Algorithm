import sys
sys.stdin = open('1005/woosteelz/2819_격자판/sample_input.txt')

dir_x = [0, 1, -1, 0]
dir_y = [1, 0, 0, -1]


def bfs(x, y, cnt, res):
    if not cnt:
        if not res in ans:
            ans.append(res)
        return

    for i in range(4):
        next_x, next_y = x + dir_x[i], y + dir_y[i]
        if 0 <= next_x < 4 and 0 <= next_y < 4:
            bfs(next_x, next_y, cnt - 1, res + graph[next_x][next_y])


for tc in range(int(input())):
    graph = [list(map(str, input().split())) for _ in range(4)]
    ans = []
    for i in range(4):
        for j in range(4):
            bfs(i, j, 6, graph[i][j])
    print(f'#{tc + 1} {len(ans)}')
