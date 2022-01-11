import sys
sys.stdin = open('input.txt')


movement = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def bfs(y,x):
    global queue
    count = 0
    # 큐가 빌때까지 반복한다.
    # 세컨드 큐까지 비어있다면 이동을 못하는것이므로 0을 리턴하게 된다.

    while queue:
        #x, y 좌표를 꺼내서
        y,x = queue.pop()
        for i, j in movement:
            dy = y+i
            dx = x+j
            if 0 <= dy < N and 0 <= dx < N:
                if box[dy][dx] == 0:
                    box[dy][dx] = 1
                    count += 1
                    queue.append[dy][dx]
                    # 도착한 경우
                if box[dy][dx] == 3:
                    return count
                    # 전부다 1로 가로막힌 경우

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    box = []
    for _ in range (N):
        box.append(list(map(int, input())))
    queue = []
    for j in range(N):
        for i in range(N):
            if box[j][i] == 2:
                queue.append((j,i))
                break
    print(bfs(j,i))
