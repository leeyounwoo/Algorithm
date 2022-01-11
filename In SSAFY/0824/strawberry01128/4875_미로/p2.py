import sys
sys.stdin = open('input.txt')

def hamsu(sy, sx):
    global answer
    result[sy][sx] = 1  # 방문 처리
    dyx = ((0, 1), (1, 0), (0, -1), (-1, 0))  # 오른쪽, 아래, 왼쪽 순서

    for dy, dx in dyx:
        ny, nx = sy + dy, sx + dx
        # 벽 생성
        if 0 <= ny <= box_size - 1 and 0 <= nx <= box_size - 1:
            if result[ny][nx] == 0:
                # 만약에 종료지점에 다다르지 않았어 그리고 가는길이야~
                hamsu(ny, nx) # 응 더가
                # 만약 도착 해버렸다면?
            elif result[ny][nx] == 3:
                answer = 1

T = int(input())
for tc in range(1,T+1):
    result = []
    box_size = int(input())
    answer = 0
    for _ in range(box_size):
        result.append(list(map(int, input())))
    # 어디서 시작할꺼야?
    for i in range(box_size):
        for j in range(box_size):
            if result[j][i] == 2:
                start_y = j
                start_x = i
                break
    sy, sx = start_y, start_x
    hamsu(sy, sx)
    print('#{} {}'.format(tc,answer))