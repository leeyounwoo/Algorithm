import sys
sys.stdin = open('input.txt')

def dfs(cnt):
    global result, info
    cnt += 1
    if cnt > N:
        temp = 0
        for i in range(W):
            for j in range(H):
                if info[j][i] != 0:
                    temp +=1
        if result > temp:
            result = temp
        return

    temp_info = [i[:] for i in info]

    for i in range(W):
        for j in range(H):
            if info[j][i] != 0:
                delete_block(j, i)
                sort_block()
                break
        dfs(cnt)
        info = [i[:] for i in temp_info]

def delete_block(y, x):
    if y < 0 or y >= H or x <0 or x >= W:
        return
    if info[y][x] == 0:
        return

    length = info[y][x] - 1
    info[y][x] = 0
    for i in range(-length, length+1):
        if i != 0:
            delete_block(y+i,x)
            delete_block(y, x+i)

def sort_block():
    for i in range(W):
        temp = []
        for j in range(H):
            if info[j][i] != 0:
                temp.append(info[j][i])
                info[j][i] = 0
        k = H - 1
        while temp:
            info[k][i] = temp.pop()
            k -= 1

T = int(input())
for tc in range(T):
    N, W, H = map(int, input().split())
    info = [list(map(int, input().split())) for _ in range(H)]
    result = W*H
    dfs(0)
    print('#{} {}'.format(tc+1, result))