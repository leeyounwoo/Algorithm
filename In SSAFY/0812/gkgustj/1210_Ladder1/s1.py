import sys

sys.stdin = open('input.txt')

def mv_left(i, j):
    # j가 0일 경우 좌표 그대로 리턴
    if j == 0:
        return i, j
    # j가 0이 아닐 경우 왼쪽이 1이 아닐 때까지 왼쪽으로 이동
    elif ladder[i][j-1]:
        return mv_left(i, j-1)
    # 더이상 왼쪽이 1이 아닐 경우 좌표 리턴
    else:
        return i, j

def mv_right(i, j):
    if j == 99:
        return i, j
    elif ladder[i][j+1]:
        return mv_right(i, j+1)
    else:
        return i, j


for _ in range(10):
    t = int(input())

    ladder = []
    for _ in range(100):
        ladder.append(list(map(int, input().split())))

    # 도착점의 좌표 구하기 ladder[i][j]
    i = 99
    j = 0
    while True:
        if ladder[i][j] == 2:
            break
        else:
            j += 1

    while i:
        i -= 1

        if j == 0:
            i, j = mv_right(i, j)
            continue
        elif j == 99:
            i, j = mv_left(i, j)
            continue
        elif ladder[i][j-1]:
            i, j = mv_left(i, j)
        elif ladder[i][j+1]:
            i, j = mv_right(i, j)

    print('#{} {}'.format(t, j))