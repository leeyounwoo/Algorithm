import sys
sys.stdin = open('input.txt')

# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 좌표, 만들고 있는 숫자, 어디 자리까지 만들었는지
def DFS2(r, c, num, idx):
    if idx == 7:
        ans.add(num)
    else:
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]

            if 0 <= nr < N and 0 <= nc < N:
                DFS2(nr, nc, num*10+arr[nr][nc], idx+1)

    return None

T = int(input())
for tc in range(1, T+1):
    N = 4
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = set()

    for i in range(N):
        for j in range(N):
            DFS2(i, j, arr[i][j], 1)

    print('#{} {}'.format(tc, len(ans)))