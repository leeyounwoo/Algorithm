import sys
sys.stdin = open('input.txt')
def hamsu(sy, sx):
    result[sy][sx] = 1  # 방문 처리
    dyx = ((0, 1), (1, 0), (0, -1), (-1, 0))  # 오른쪽, 아래, 왼쪽 순서

    for dy, dx in dyx:
        ny, nx = sy + dy, sx + dx
        # 갈 수 있는 위치인지 판별
        if 0 <= ny <= box_size - 1 and 0 <= nx <= box_size - 1:
            if result[ny][nx] == 0:
                # 만약에 길을 찾았으면?
                return hamsu(ny, nx) # 계속 가세용~
            elif result[ny][nx] == 3:
                return 1
    return 0
 # -> 문제점 길이 2개가 있는데 짧은길로가버리면? 3 0 0 0  2  0 0
 # 철수야 나 도착했는데 뭐없는데? (철수는 먼 길로 3찾는중)
 # 응 이미 길 없다고 표시했어~ (철수 3찾다가 놀람)
T = int(input())
for tc in range(1,T+1):
    result = []
    box_size = int(input())
    answer = 0
    for _ in range(box_size):
        result.append(list(map(int, input())))
    for i in range(box_size):
        for j in range(box_size):
            if result[j][i] == 2:
                start_y = j
                start_x = i
                break
    sy, sx = start_y, start_x
    ans = hamsu (sy, sx)
    print('#{} {}'.format(tc,ans))