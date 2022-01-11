import sys
sys.stdin = open("input.txt")
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    corridor = [0] * 400
    for _ in range(N):
        x, y = map(int, input().split())
        if x <= y:
            start = (x-1) // 2
            end = (y-1) // 2
        else:
            start = (y-1) // 2
            end = (x-1) // 2
        for i in range(start, end+1):
            corridor[i] += 1
    max_time = 0
    for i in corridor:
        if i > max_time:
            max_time = i
    print('#{} {}'.format(tc, max_time))
