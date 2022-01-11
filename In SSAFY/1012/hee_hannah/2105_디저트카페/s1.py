import sys
sys.stdin = open('input.txt')

'''
상: -1 하 +1 우:+1 좌: -1 

우하 좌하 좌상 우상 (1,1) (-1,1) (-1,-1) (1,-1)
'''
i1 = [1, -1, -1, 1]
j1 = [1, 1, -1, -1]

def find(target, x, y):
    num = [-1]
    a = x
    b = y
    visited = [[0] * n for _ in range(n)]
    equal_check = [target]
    cnt = 1
    while True:
        for k in range(3):
            if (0 <= x + i1[k] <= n-1 and 0 <= y + i1[k] <= n-1
                and li[x + i1[k]][y + i1[k]] != equal_check and visited[x + i1[k]][y + i1[k]] !=1):
                x += i1[k]
                y += j1[k]
                visited[x + i1[k]][y + i1[k]] = 1
                equal_check.append(li[x + i1[k]][y + i1[k]])
                cnt += 1
                x = x + i1[k]
                y = y + i1[k]
            else:
                k += 1
                k += 1
            if k == 3 and 0 <= x + i1[k] <= n-1 and 0 <= y + i1[k] <= n-1 and x + i1[k] == a and y + i1[k] == b:
                num.append(cnt)
                break

    return max(num)




t = int(input())
for tc in range(1, t+1):
    print('#{}'.format(tc), end=" ")
    n = int(input())
    li = [list(map(int, input().split())) for _ in range(n)]

    # num = []
    for i in range(n):
        for j in range(n):
            target = li[i][j]
            x = i
            y = j
    print(find(target,x,y))