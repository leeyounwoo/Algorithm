import sys
sys.stdin = open('input.txt')
di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

def find_way(maze):
    stack = []
    check = [[False] * N for _ in range(N)]
    stack.append((0, 0))
    ans = -1

    while stack:
        now_i, now_j = stack.pop()
        check[now_i][now_j] = True
        if now_i == N-1 and now_j == N-1:
            ans = 1
            break
        else:
            flag = 0
            for i in range(4):
                next_i, next_j = now_i + di[i], now_j + dj[i]
                if 0 <= next_i < N and 0 <= next_j < N and not check[next_i][next_j] and not maze[next_i][next_j]:
                    stack.append((next_i, next_j))
                    flag += 1



    return ans



N = int(input())
maze = [list(map(int, input().split())) for _ in range(N)]
print(find_way(maze))
