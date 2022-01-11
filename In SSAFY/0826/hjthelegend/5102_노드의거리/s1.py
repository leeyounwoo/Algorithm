import sys
sys.stdin = open('input.txt')
from collections import deque

def road_finder(s):
    queue = deque([])
    queue.append(s)
    visited[s] = 0 # 처음 시작 간선을 안지났으니 0

    while queue:
        pop = queue.popleft()

        for i in arr[pop]:
            if visited[i] == -1:
                queue.append(i)
                visited[i] = visited[pop] + 1

# 6 5
# 1 6
t = int(input())
for tc in range(1, t+1):
    v, e = map(int, input().split())
    arr = [[] for _ in range(v+1)]

    for _ in range(e):
        one, two = map(int, input().split())
        arr[one].append(two)
        arr[two].append(one)

    s, g = map(int, input().split())

    visited = [-1] * (v+1) # 가보지도 않은 곳은 -1
    road_finder(s)

    answer = 0

    if visited[g] != -1:
        answer = visited[g]

    print(visited)

    print('#{} {}'.format(tc, answer))
