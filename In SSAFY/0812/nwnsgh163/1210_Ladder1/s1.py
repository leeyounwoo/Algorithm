import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T+1):
    number = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]     # 100*100 행렬

    y, x = 99, 0    # ex) 99, 99
    for i in range(100):        # 아래에서 위로 올라가는 방식 왜냐하면 도착값이 2이므로
        if arr[99][i] == 2:
            x = i               # 도착지점 x 값

     moves = [[y, x]]
    # 리스트가 비어있다는 말은
    # 더 이상 갈 곳이 없다는 뜻
    while moves:
            y, x = moves.pop()
            ladder[y][x] = 0

            if y == 0:
                result = x
                break

            dyx = ((0, -1), (0, 1), (-1,0))        #왼, 오 위 순서
            for i in range(3):
                dy, dx = dyx[i]
                ny, nx = y +dy, x + dx

                if 0 <= nx <= 99 and 0 <= ny <= 99:
                    if ladder[ny][nx]:
                        moves.append( [ny, x] )
                        break


    print('#{} {}'.format(tc, result))




    #         break               # 찾았으면 멈춰!
    #
    # y = 99                      # 도착 y 값 아래에서 부터 시작하므로 99
    #
    # while True:                 # 왼쪽, 오른쪽으로 이동하고 없을시 위로 이동하도록 설정
    #     if x > 0 and arr[y][x-1]:
