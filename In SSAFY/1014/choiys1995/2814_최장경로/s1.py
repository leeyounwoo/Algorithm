import sys
sys.stdin = open('input.txt')

def dfs(idx,cnt):
    global max_num
    # visit[idx] 값을 이용해 갔다온 정점 체크
    visit[idx] = True
    if cnt > max_num:
        max_num = cnt
    for i in s[idx]:
        if not visit[i]:
            dfs(i, cnt+1)
            visit[i] = 0

T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())
    # 연결 리스트 만들기
    s = [[] for i in range(n + 1)]
    for i in range(m):
        x, y = map(int, input().split())
        s[x].append(y)
        s[y].append(x)
    # 최장 경로를 저장할 변수
    max_num = 0

    # 모든 정점마다 dfs를 해보면서 최장 경로 따져보기
    for i in range(1, n+1):
        visit = [0] * (n+1)
        dfs(i,1)
    print('#{} {}'.format(tc, max_num))