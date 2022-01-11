import sys
sys.stdin = open('input.txt')
def dfs(idx):
    global result, cnt

    if idx >= len(bus)-1:
        if cnt <= result:
            result = cnt
        return

    if result <= cnt:
        return

    for i in range(idx+bus[idx], idx, -1):
        cnt += 1
        dfs(i)
        cnt -= 1



T = int(input())
for tc in range(1, T+1):
    bus = list(map(int, input().split()))
    bus.append(0)
    num = bus.pop(0)
    result = 100000
    cnt = 0
    dfs(0)
    print('#{} {}'.format(tc, result-1))
