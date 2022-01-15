import sys
from collections import deque


def input():
    return sys.stdin.readline().rstrip()


# bfs 방법으로 물고기를 먹으러 가는 거리 구하기
di, dj = [0, 0, 1, -1], [1, -1, 0, 0]
def findDistance(start_i, start_j, end_i, end_j, shark_size, n):
    check = [[False] * n for _ in range(n)]
    q = deque([[start_i, start_j, 0]])
    check[start_i][start_j] = True
    while q:
        now_i, now_j, time = q.popleft()
        if now_i == end_i and now_j == end_j:
            return time
        for k in range(4):
            next_i, next_j = now_i + di[k], now_j + dj[k]
            if 0 <= next_i < n and 0 <= next_j < n and not check[next_i][next_j]:
                # 크기가 작거나 같거나 상어가 있던 위치(빈 공간이나 다름 없음)는 이동할 수 있음
                if sea[next_i][next_j] <= shark_size or sea[next_i][next_j] == 9:
                    q.append([next_i, next_j, time + 1])
                    check[next_i][next_j] = True

    # 해당 물고기를 먹으러 갈 수 있는 길이 없는 경우
    return False


n = int(input())
sea = []
fishes = {}
shark = ()
for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(len(temp)):
        if temp[j] == 9:
            shark = (i, j)
        elif temp[j]:
            if temp[j] not in fishes:
                fishes[temp[j]] = [(i, j)]
            else:
                fishes[temp[j]].append((i, j))
    sea.append(temp)

time = 0
shark_size = 2
eat_fish = 0
fish_sizes = sorted(list(fishes.keys()))
while True:
    # 아기 상어보다 크기가 작은 물고기들
    eatable_fishes = []
    for size in fish_sizes:
        if size < shark_size:
            eatable_fishes.extend(fishes[size])

    if eatable_fishes:
        distance = 1000
        goal_i, goal_j = 100, 100
        for fish_i, fish_j in eatable_fishes:
            temp_distance = findDistance(shark[0], shark[1], fish_i, fish_j, shark_size, n)
            # 해당 물고기로 갈 수 있는 길이 없는 경우엔 다음 반복으로 넘어간다.
            if temp_distance == False:
                continue
            else:
                # 만약 거리가 더 짧다면 그 물고기를 먹으러 감
                if temp_distance < distance:
                    distance = temp_distance
                    goal_i, goal_j = fish_i, fish_j
                # 만약 거리가 같다면
                if temp_distance == distance:
                    # 더 위에 있는 물고기
                    if fish_i < goal_i:
                        goal_i, goal_j = fish_i, fish_j
                    # 높이가 같다면 더 왼쪽에 있는 물고기
                    elif fish_i == goal_i and fish_j < goal_j:
                        goal_i, goal_j = fish_i, fish_j

        # 초기화 변수가 그대로 있는 경우
        # 아기 상어보다 작은 물고기는 있지만 먹으러 갈 수 없는 경우
        if goal_i == 100 and goal_j == 100:
            break
        # 물고기 잡아먹기
        time += distance
        eat_fish += 1
        if eat_fish == shark_size:
            eat_fish = 0
            shark_size += 1
        shark = (goal_i, goal_j)
        fishes[sea[goal_i][goal_j]].remove((goal_i, goal_j))


    # 크기가 작은 물고기가 없는 경우
    else:
        break

print(time)

