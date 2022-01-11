import sys
sys.stdin = open('input.txt')

# i,j 위:  0 -1 아래: 0 +1 오른: +1 0 왼: -1 0
def find(a, b):
    delta = [[0, -1], [0, 1], [1, 0], [-1, 0]]
    cnt = 0
    work = 1
    visited[a][b] = 1
    for k, r in delta:
        if visited[a+k][b+r] == 0 and li[a][b] > li[a+k][b+r] and a+k < size and b+r < size:
            visited[a+k][b+r] = 1
            cnt += 1
            a, b = a+k, b+r
        elif visited[a+k][b+r] == 0 and li[a][b] <= li[a+k][b+r] and a+k < size and b+r < size:
            if work >= 1 and depth >= 1:
                work = 0
                height = 1
                while depth > height:
                    li[a + k][b + r] - height
                    height += 1
                    if li[a][b] > li[a + k][b + r] - height:
                        visited[a + k][b + r] = 1
                        cnt += 1
                        a, b = a + k, b + r
                        break
            elif work < 1:
                continue
    print(cnt)

t = int(input())
for tc in range(1, t+1):
    print('#{}'.format(tc))
    size, depth = map(int, input().split())
    li = [list(map(int, input().split())) for _ in range(size)]
    visited = [[0]*size for _ in range(size)]
    max_li = []
    for i in li:
        max_li.append(max(i))
    max_num = max(max_li)
    count = []
    for i in range(size):
        for j in range(size):
            if li[i][j] == max_num:
                a = i
                b = j
                find(a, b)

