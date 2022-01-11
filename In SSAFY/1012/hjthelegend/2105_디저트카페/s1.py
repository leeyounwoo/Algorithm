import sys
sys.stdin = open('input.txt')

# 대각선 이동
# 최대한 많은 디저트의 종류

# 우하, 좌하, 좌상, 우상
dxy = [(1, 1), (1, -1), (-1, -1), (-1, 1)]

def more(x, y, count):
    stack = [(x, y, count)]
    result = {}
    max_count = 0
    while stack:
        x, y, count = stack.pop()
        for i in range(4):
            nx = dxy[i][0] + x
            ny = dxy[i][1] + y
            if -1 < nx < n and -1 < ny < n:
                if dessert[nx][ny] not in result:
                    result[dessert[nx][ny]] = 1
                    count += 1
                    stack.append((nx, ny, count))
                    max_count = max(count, max_count)
    
    return max_count
  
t = int(input())
for tc in range(1, t+1):
    n = int(input())
    dessert = [list(map(int, input().split())) for _ in range(n)]
    answer = 0
    visited = [0] * 101
    for i in range(n):
        count = 1
        for j in range(n):
            answer = max(answer, more(i, j, count))
    print('#{} {}'.format(tc, answer))

def tour(x, y, dir, count):
    global result, nx, ny

    if 0 > x or x > n-1 or y > n-1 or y < 0:
        return