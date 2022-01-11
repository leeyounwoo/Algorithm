import sys
sys.stdin = open('input.txt')



for tc in range(10):
    T = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]

    for i in range(100):
        if ladder[99][i] == 2:
            x = i
    y = 99

    moves = [[y, x]]
    # 리스트가 비어있다는 말은
    # 더 이상 갈 곳이 없다는 뜻
    result = 0
    while moves:
        y, x = moves.pop()
        ladder[y][x] = 0

        if y == 0:
            result = x
            break
        dyx = ((0, -1), (0, 1), (-1, 0))
        for i in range(3):
            dy, dx = dyx[i]
            ny, nx = y + dy, x + dx

            if 0<=nx <=99 and 0<=ny<=99 and ladder[ny][nx]:
                moves.append([ny, x])
                break
    print(result)