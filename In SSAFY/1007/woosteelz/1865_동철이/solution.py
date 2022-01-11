def get_max(idx, res):
    global ans
    if idx == N:
        ans = max(ans, res)
        return

    if ans >= res:
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            get_max(idx+1, res * (percent[idx][i]/100))
            visited[i] = False


for tc in range(int(input())):
    N = int(input())
    percent = [list(map(int, input().split())) for _ in range(N)]
    visited = [False for _ in range(N)]
    ans = float('-inf')
    get_max(0, 100)
    ans = round(ans, 6)
    print(f'#{tc+1} {ans:.6f}')
