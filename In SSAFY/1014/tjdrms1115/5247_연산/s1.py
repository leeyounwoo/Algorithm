import sys
sys.stdin = open('input.txt')

T = int(input())

answer = []
for tc in range(1, T + 1):

    N, M = map(int, input().split())

    q = []
    visited = set()

    q.append((N, 0))

    result = 0
    while True:

        v, rank = q.pop(0)
        if v == M:
            result = rank
            break
        if v not in visited:
            visited.add(v)

            if 0 < v + 1 <= 1000000:
                q.append([v + 1, rank + 1])
            if 0 < v - 1 <= 1000000:
                q.append([v - 1, rank + 1])
            if 0 < v * 2 <= 1000000:
                q.append([v * 2, rank + 1])
            if 0 < v - 10 <= 1000000:
                q.append([v - 10, rank + 1])

    answer.append(result)

for tc in range(1, T + 1):
    print(f'#{tc} {answer[tc-1]}')
