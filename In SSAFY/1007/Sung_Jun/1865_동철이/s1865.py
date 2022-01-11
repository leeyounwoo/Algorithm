import sys
sys.stdin = open('input.txt')

def DFS(y, sum):
    global result

    if y == N:
        if result < sum:
            result = sum
        return

    if result < sum:
        return

    for x in range(N):
        if not visited[x]:
            visited[x] = True
            DFS(y+1, sum + case[y][x])
            visited[x] = False

T = int(input())
for tc in range(T):
    N = int(input())
    case = [list(map(int, input().split())) for _ in range(N)]
    print(case)
    visited = [0]*N
    result = 0
    DFS(0, 0)
    print(result)
