import sys
sys.stdin = open('input.txt')

# N명의 직원
# N개의 할 일
# 주어진 일이 모두 성공할 확률 '최댓값'

def dfs(idx, result):
    global answer

    if idx == n and result > answer:
        answer = result
        return

    # 볼 필요가 없음
    if answer >= result:
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = 1
            dfs(idx+1, result * per[i][idx]/100)
            visited[i] = 0

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    per = [list(map(int, input().split())) for _ in range(n)]
    visited = [0] * n
    answer = 0
    dfs(0, 1)

    print('#{} {:6f}'.format(tc, answer*100))