import sys
sys.stdin = open('input.txt')

def prunning(idx, temp):
    global ans
    if idx == N:
        if temp < ans:
            ans = temp
        return

    if temp > ans:
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            prunning(idx + 1, temp + square[idx][i])
            visited[i] = False


TC = int(input())
for tc in range(TC):
    N = int(input())
    square = [list(map(int, input().split())) for _ in range(N)]
    visited = [False for _ in range(N)]
    ans = 987654321

    prunning(0, 0)

    print('#{} {}'.format(tc+1, ans))