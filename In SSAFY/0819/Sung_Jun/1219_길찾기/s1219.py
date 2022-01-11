import sys
sys.stdin = open('input.txt')

T = 10

for _ in range(T):
    tc, total_len = map(int, input().split())
    temp = list(map(int, input().split()))
    start, end = 0, 99

    check = {key : [] for key in range(end+1)}
    for tem in range(0, len(temp)-1, 2):
        check[temp[tem]].append(temp[tem+1])

    stack = [start]
    visited = []
    result = 0
    while stack:
        v = stack.pop()
        if v == end:
            result = 1
            break
        if v not in visited:
            visited.append(v)
            for w in check[v]:
                stack.append(w)
    print('#{} {}'.format(tc, result))


