import sys
sys.stdin = open('input.txt')

def money(n, items, total):
    global ans

    if total >= ans:
        return

    if n == N:
        ans = min(ans, total)
        return

    for i in range(N):
        if i not in items:
            items.append(i)
            money(n+1, items, total+matrix[n][i])
            items.pop()


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    ans = 1500
    money(0, [], 0)
    print('#{} {}'.format(tc, ans))
