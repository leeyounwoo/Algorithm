def get_min(idx, res):
    global ans
    if idx == N:
        ans = min(ans, res)
        return
    if res > ans:
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            get_min(idx+1, res + factory[idx][i])
            visited[i] = False


for tc in range(int(input())):
    N = int(input())
    factory = [list(map(int, input().split())) for _ in range(N)]
    visited = [False for _ in range(N)]
    ans = float('inf')
    get_min(0, 0)
    print(f'#{tc+1} {ans}')
