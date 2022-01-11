T = 10

for tc in range(1, T+1):
    n = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]

    y, x = 99, 0
    for i in range(100):
        if ladder[99][i] == 2:
            x = i

    moves = [[y, x]]
    # 리스트가 비어있다는 말은
    # 더 이상 갈 곳이 없다는 뜻
    result = 0
    while moves:
        y, x = moves.pop()
        ladder[y][x] = 0

        if y == 0 :
            result = x
            break

        dyx = ((0, -1), (0, 1), (-1, 0))  # 왼, 오, 위 순
        for i in range(3):
            dy, dx = dyx[i]
            ny, nx = y + dy, x + dx

            if 0 <= nx <= 99 and 0 <= ny <= 99:
                if ladder[ny][nx]:
                    moves.append([ny, x])
                    break

    print(f'#{} {}'.format(tc, result))
