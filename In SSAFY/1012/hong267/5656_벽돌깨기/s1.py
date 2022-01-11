import sys

sys.stdin = open('input.txt')

def game(n, list0):
    global result
    if n == 0:
        cnt = 0
        for ri in range(H):
            for rj in range(W):
                if list0[ri][rj]:
                    cnt += 1
        result.append(cnt)
        return

    for j in range(W):
        for i in range(H):
            if list0[i][j] != 0:
                temp_blocks = list0[:]
                remove_blocks(i, j, temp_blocks)
                down_blocks(temp_blocks)
                game(n-1, temp_blocks)

def down_blocks(list2):
    for ti in range(H - 1):
        for tj in range(W):
            if list2[ti+1][tj] == 0 and list2[ti][tj] != 0:
                temp = list2[ti][tj]
                list2[ti+1][tj] = temp
                list2[ti][tj] = 0

def remove_blocks(i, j, list1):
    distance = list1[i][j]
    while distance:
        distance -= 1
        for d in range(4):
            ni = i + di[d] * distance
            nj = j + dj[d] * distance
            if 0 <= ni < H and 0 <= nj < W:
                if list1[ni][nj] != 0:
                    if ni == i and nj == j:
                        list1[ni][nj] = 0
                        break
                    elif list1[ni][nj]:
                        remove_blocks(ni, nj, list1)


T = int(input())

for tc in range(1, T+1):
    N, W, H = map(int, input().split())
    blocks = [list(map(int, input().split())) for _ in range(H)]

    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    result = []
    game(N, blocks)

    print(result)