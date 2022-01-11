import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]

    # 델타를 이용한 2차원 배열 탐색
    di = [0, 1, 0, -1]      # 아래 오른쪽 위 왼쪽
    dj = [1, 0, -1, 0]
    total = 0

    # 반복문을 통해 5 * 5 배열 만들기
    for i in range(5):
        for j in range(5):
            for d in range(4):
                ni = i + di[d]
                nj = j + dj[d]
                if 0 <= ni < len(arr) and 0 <= nj < len(arr):
                    total += abs(arr[i][j] - arr[ni][nj])

    print('#{} {}'.format(tc,total))


