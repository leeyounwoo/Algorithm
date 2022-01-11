import sys
sys.stdin = open('input.txt')

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
def dfs(x, y, num, c):
    if c == 7:
        if num not in answers:
            answers.add(num)
        return

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx <= 3 and 0 <= ny <= 3:
            dfs(nx, ny, num + matrix[nx][ny], c + 1)


for tc in range(1, 1+int(input())):
    matrix = [input().split() for _ in range(4)]
    answers = set()
    for i in range(4):
        for j in range(4):
            dfs(i, j, matrix[i][j], 1)

    print('#{} {}'.format(tc, len(answers)))