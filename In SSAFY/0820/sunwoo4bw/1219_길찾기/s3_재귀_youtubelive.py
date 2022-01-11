def DFS(v):
    global ans
    if v == 99:
        ans = 1  # 주의! 저기 저 밑에 있는 ans와는 달라 그래서 global 키워드로 같다고 만들어 줘야 해
        return
    visited[v] = 1
    for w in range(100):
        if not visited[w] and adj_arr[v][w]:  # 너와 나 연결되어 있니? 라고 체크해줘야 해
            DFS(w)


for _ in range(10):
    tc, N = map(int, input().split())
    road = list(map(int, input().split()))

    adj_arr = [[0] * 100 for _ in range(100)]
    for i in range(N):
        adj_arr[road[2 * i]][road[2 * i + 1]] = 1
    visited = [0] * 100
    ans = 0

    DFS(0)
    print("{} {}".format(tc, ans))
