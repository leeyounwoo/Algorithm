import sys


def input():
    return sys.stdin.readline().rstrip()


def dp(now, end, flag):
    global answer
    print(flag, now)
    if now == end:
        answer = flag
        return
    temp_r = cost[now][0] + min(flag[1], flag[2])
    temp_g = cost[now][1] + min(flag[0], flag[2])
    temp_b = cost[now][2] + min(flag[0], flag[1])
    dp(now+1, end, [temp_r, temp_g, temp_b])



sys.stdin = open('input.txt')
n = int(input())
cost = [list(map(int, input().split())) for _ in range(n)]
answer = []
dp(0, n, [0, 0, 0])

print(min(answer))
