def dfs(sy, sx, path):
    #global path 이렇게해서 해도 ㄱㅊ 밑에 path []해두고,,
    maze[sy][sx] = 1 # 방문처리
    dyx = ((0, 1), (1, 0), (0, -1))  # 오른쪽 아래 왼쪽 순서

    for dy, dx in dyx:
        ny, nx = sy + dy, sx + dx
        # 갈 수 있는 위치인지 판별
        if 0 <= ny <= N - 1 and 0 <= nx <= N - 1:
            if maze[ny][nx] == 0:
                # 만약에 종료 지점에 다다르면
                if ny == N - 1 and nx == N - 1:
                    print(path)
                    return
                dfs(ny, nx, path + [[ny, nx]]) # 짝이 지어진 리스트를 담고싶으니까 리스트 한번 더 감싼것


N = int(input())
maze = [list(map(int, input().split())) for _ in range(N)]
sy, sx = 0, 0
# path = []
result = dfs(sy, sx, [])  # 재귀는 스택이없기때문에 저장할곳 없으니 처음부터 빈리스트 지정..

print(result)

