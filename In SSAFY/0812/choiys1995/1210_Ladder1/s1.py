import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    arr = [list(map(int, input().split())) for _ in range(100)]

    # 2부터 시작하기
    for i in range(100):
        if arr[99][i] == 2:
            # 도착 col지점 지정
            col = i
            break # 찾으면 멈춤
    # 도착 row지점 지정
    row = 99

    while True:
        # 왼쪽으로 가기
        if col > 0 and arr[row][col-1]:
            while col > 0 and arr[row][col-1]:
                col -= 1

        #오른쪽으로 가기
        elif col < 99 and arr[row][col+1]:
            while col < 99 and arr[row][col+1]:
                col += 1

        #위로가기
        row -= 1
        #도착
        if row == 0:
            break

    print('#{} {}'.format(tc,col))