import sys
sys.stdin = open('input.txt')
def dfs(current):
    global total, min_sum

    if total < min_sum:
        visited[current] = True

        if False not in visited:
            total += battery[current][0]
            if total < min_sum:
                min_sum = total
            total -= battery[current][0]
        else:
            for next in range(N):
                if visited[next] == False:
                    total += battery[current][next]
                    dfs(next)
                    total -= battery[current][next]

        visited[current] = False


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    battery = [list(map(int, input().split())) for _ in range(N)]
    visited = [0 for _ in range(N)]
    min_sum = 10000
    total = 0
    dfs(0)
    print('#{} {}'.format(tc, min_sum))
