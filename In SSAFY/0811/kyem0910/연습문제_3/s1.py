import sys

sys.stdin = open("input.txt")

T = int(input())
for tc in range(T):
    N = int(input())
    input_arr = []
    for _ in range(N):
        input_arr += list(map(int, input().split())) 
    input_arr.sort() 
    # 1차원 배열에 오름차순으로 정렬한 뒤, 요소를 순서대로 2차원 배열에 넣으면 된다.

    arr = [[0] * N for _ in range(N)] # 저장할 배열 = 결과
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    direction = 0  # 0=우 1=하 2=좌 3=상
    i = j = 0  # 처음 위치

    for num in range(0, N ** 2):
        arr[i][j] = input_arr[num]

        i += dy[direction]  # 일단 진행시켜본다.
        j += dx[direction]

        if i >= N or i < 0 or j >= N or j < 0 or arr[i][j] != 0:  # 진행시킨 결과에 문제가 발생하면
            # 리스트를 벗어나거나 이미 숫자를 갱신했을 경우
            i -= dy[direction]  # 했던 작업을 되돌린다.
            j -= dx[direction]

            direction += 1
            if direction > 3:  # 0 1 2 3 다음에 다시 0으로
                direction = 0

            i += dy[direction]  # direction 변경후 다시 진행시킨다.
            j += dx[direction]

    print("#{}".format(tc + 1))
    for num in arr:
        print(*num)