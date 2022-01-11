import sys
sys.stdin = open("input.txt")

T = int(input())

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for test_case in range(1,T+1):
    N = int(input())
    result = [[0]*N for _ in range(N)]
# 내가 바로 다음으로 갈 위치
    dir_stat = 0 # 초기 방향 오른쪽
    x, y = 0, 0 #초기 위치

    # N을 받았을때 그걸 제곱하는 1씩 증가하는갯수를 만들고
    for Snail_square in range(1,N**2+1):
    # 여기서 dx dy를 이용해서 N을 넘지않는선에서 index로 result[dx][dy]로 어떻게좀해봐!
        result[y][x] = Snail_square
        x = x + dx[dir_stat]
        y = y + dy[dir_stat]
        if x < 0 or y < 0 or x >= N or y >= N or result[y][x] != 0:

            x = x - dx[dir_stat]
            y = y - dy[dir_stat]
            dir_stat = (dir_stat+1) % 4
            x = x + dx[dir_stat]
            y = y + dy[dir_stat]

    print('#{}'.format(test_case))
    for i in result:
        print(*i)


            # 00 01 02
            # 10 11 12
            # 20 21 22

    #     for real_delta in range(N):
    #         for delta in range(N):
    #             result[delta+dy[real_delta]][delta+dx[real_delta]] = Snail_square
    #     if dx < N:
    #         for delta in range(N):
    #         result[dx[delta]][dy[delta]] = Snail_square
    #         dx += 1


    # 그걸 인덱스 값으로 집어서 넣어! 인덱스값은 dx 값 이랑 dy값이용해서
