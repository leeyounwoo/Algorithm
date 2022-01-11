import sys
sys.stdin = open('input.txt')

T = int(input())     # 10
for tc in range(1, T +1):  # tc 1부터
    # 달팽이집 만들기
    N = int(input())
    shell = [[0]*N for _ in range(N)]

    # 인덱스를 활용해서 방향전환을 하고 싶을 때는
    # dx, dy리스트를 만들고 접근
    # 오른쪽, 아래, 왼쪽, 위
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    # 내가 지금 달리고 있는 방향의 변수를 정해줘야 해
    dir_stat = 0  # 초기 방향 오른쪽
    x, y = 0, 0  # 처음 나의 위치 fix

    total_number = N*N

    # 반복문 돌면서 shell에 n 추가
    for n in range(1, total_number + 1):
        shell[y][x] = n
        # 다음 방향으로 이동
        x += dx[dir_stat]
        y += dy[dir_stat]

        # 벽 만들어주기
        # 앞으로 가다가 방향 틀어야 해
        # index 벗어나거나 이미 숫자가 있거나
        if x >= N or y >= N or shell[y][x] != 0:
            x -= dx[dir_stat]
            y -= dy[dir_stat]
            dir_stat = (dir_stat+1) % 4

            x += dx[dir_stat]
            y += dy[dir_stat]

    print('#{}'.format(tc))
    for s in shell:
        print(*s)




