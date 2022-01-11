import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    N = int(input())
    case = [input() for _ in range(N)]
    check_box = [[0]*N for _ in range(N)]
    dyx = ((0, 1), (1, 0),  (0, -1), (-1, 0))

    stack = []
    for i in range(N):
        for j in range(N):
            if case[i][j] == '2':
                stack.append((i, j))

    result = 0
    while stack:
        v = stack.pop()
        if int(case[v[0]][v[1]]) == 3:
            result = 1

        for dy, dx in dyx:
            ny = v[0]+dy
            nx = v[1]+dx
            if 0 <= ny <= N-1 and 0 <= nx <= N-1:
                if case[ny][nx] == '0':
                    if check_box[ny][nx] == 0:
                        stack.append((ny, nx))
                        check_box[v[0]][v[1]] += 1

    print(result)

