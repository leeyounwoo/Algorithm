def dfs(idx, temp):
    global answer
    if answer < temp:
        return
    if idx >= N:
        answer = temp
        return
    count = bus_stop[idx]
    for i in range(count, 0, -1):
        dfs(idx+i, temp+1)


TC = int(input())
for tc in range(1, TC + 1):
    bus_stop = list(map(int, input().split()))
    N = bus_stop.pop(0) - 1
    answer = float("inf")
    dfs(0, -1)
    print(f"#{tc} {answer}")
