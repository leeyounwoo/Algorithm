'''
0, 0에서 7, 7까지 지나가는 모든 경로를 출력하시오

8
0 0 1 1 1 1 1 1
1 0 0 0 0 0 0 1
1 1 1 0 1 1 1 1
1 1 1 0 1 1 1 1
1 0 0 0 0 0 0 1
1 0 1 1 1 1 1 1
1 0 0 0 0 0 0 0
1 1 1 1 1 1 1 0
'''

# # 교수님 풀이 1


# def dfs(sy, sx):
#     # 핵심 아이디어
#     # 다음 지점으로 갈 떄 "필요할 정보를 같이 가져가기"
#     stack = [(sy, sx, [])]
#
#     dyx = ((0, 1), (1, 0), (0, -1)) # 오른쪽, 아래, 왼쪽 순서
#     while stack:
#         # 현재 방문할 위치
#         y, x, path = stack.pop()
#         maze[y][x] = 1  # 방문 체크
#
#         for dy, dx in dyx:
#             ny, nx = y + dy, x + dx
#             # 갈 수 있는지 판단
#             # 1. 새로운 위치(ny, nx)가 배열의 범위를 벗어나지 않는지?
#             # 2. 새로운 위치(ny, nx)가 벽이 아닌지?
#             if 0 <= ny <= N-1 and 0 <= nx <= N-1:
#                 if maze[ny][nx] == 0:
#                     # 종료지점에 도착하면 경로 반환
#                     if ny == N-1 and nx == N-1:
#                         return path
#                     # 다음에 방문할 곳으로 스택에 추가
#                     stack.append((ny, nx, path + [[y, x]]))
#
#
# N = int(input())
# maze = [list(map(int, input().split())) for _ in range(N)]
# sy, sx = 0, 0
#
# result = dfs(sy, sx)
# print(result)

# 교수님 풀이 2


def dfs(sy, sx, path):
    maze[sy][sx] = 1  # 방문 처리
    dyx = ((0, 1), (1, 0), (0, -1)) # 오른쪽, 아래, 왼쪽 순서
    for dy, dx in dyx:
        ny, nx = sy + dy, sx + dx
        # 갈 수 있는 위치인지 판별
        if 0 <= ny <= N-1 and 0 <= nx <= N-1:
            if maze[ny][nx] == 0:
                # 만약에 종료지점에 다다르면
                if ny == N-1 and nx == N-1:
                    print(path)
                    return
                dfs(ny, nx, path + [[ny, nx]])


N = int(input())
maze = [list(map(int, input().split())) for _ in range(N)]
sy, sx = 0, 0

result = dfs(sy, sx, [])
print(result)


# def promising(N, board, i, j):
#     if (0 <= i < N) and (0 <= j < N) and board[i][j] == 0:
#         return True
#     return False
# 
# 
# def dfs(N, board, delta, i, j):
#     if promising(N, board, i, j):
#         if (i, j) == (N-1, N-1):
#             return [(i, j)]
#         else:
#             board[i][j] = 1
#             for a in range(len(delta)):
#                 di, dj = delta[a]
#                 path = dfs(N, board, delta, i+di, j+dj)
#                 if path:
#                     return [(i, j)] + path
#             board[i][j] = 0
#     return None
# 
# 
# N = int(input())
# 
# board = [list(map(int, input().split())) for _ in range(N)]
# delta = [[-1, 0], [1, 0], [0, -1], [0, 1]]
# 
# result = dfs(N, board, delta, 0, 0)
# 
# print(result)
