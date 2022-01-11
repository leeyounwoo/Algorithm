import sys
sys.stdin = open('1244_input.txt')

def solve(N, k):
    global result
    total = int(''.join(map(str, num)))

    if total in visited[k]:
        return
    visited[k].add(total)

    if k == goal:
        if total > result:
            result = total
        return

    for i in range(N - 1):
        for j in range(i + 1, N):
            num[i], num[j] = num[j], num[i]
            solve(N, k + 1)
            num[i], num[j] = num[j], num[i]


T = int(input())
for tc in range(1, 1 + T):
    num, goal = input().split()
    num = list(map(int, num))
    goal = int(goal)
    visited = [set() for _ in range(goal + 1)]

    result = 0
    solve(len(num), 0)
    print(f'#{tc} {result}')













