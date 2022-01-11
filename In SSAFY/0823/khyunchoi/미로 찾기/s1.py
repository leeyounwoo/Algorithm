def dfs(r, c):
    stack = []
    stack.append((r, c))

    while stack:
        r, c = stack.pop()

        if visited[r][c] == 0:
            visited[r][c] = 1
            print((r, c), end=' ')
            if (r, c) == (7, 7):
                return

            for i in range(4):
                if 0 <= r+dr[i] < 8 and 0 <= c+dc[i] < 8 and mazeArray[r+dr[i]][c+dc[i]] == 0 and visited[r+dr[i]][c+dc[i]] == 0:
                    stack.append((r+dr[i], c+dc[i]))


mazeArray = [
    [0, 0, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 0, 1, 1, 1, 1],
    [1, 1, 1, 0, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 0],
]
visited = [[0]*8 for _ in range(8)]

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

dfs(0, 0)
