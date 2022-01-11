import sys
sys.stdin = open('input.txt')

def dfs(v):
    stack = []
    stack.append(v) # 시작 지점 스택에 삽입

    while stack: # 순회 시작!
        v = stack.pop()

        if visited[v] == 0:
            visited[v] = 1 # 방문 표기
            print(v, end=" ") # 현재 방문한 노드 출력

            for w in range(1, V+1): # 인접 노드 순회
                if G[v][w] == 1 and visited[w] == 0: # 인접 노드 중 갈 수 있는 곳이라면
                    stack.append(w)

testcase, long = list(map(int,input().split()))
way = list(map(int, input().split()))


node_start = way[0]
node_end = 99
# DFS 시작
result = 0
stack = [way[0]] # 내가 다음에 갈 위치를 저장
visited = []
while stack:
    next_node = stack.pop()
    if next_node == 99:
        result = 1 # 목표에 도달한 경우
        break
    if next_node not in visited: # 방문한 적이 없으면
        visited.append(next_node) # 방문 체크
        for nb in adjacent[next_node]:
            stack.append(nb)
print('#{} {}'.format(testcase, result))



# -교수님 풀이
for _ in range(1):
    tc, N = map(int, input().split())
    road = list(map(int, input().split()))

    # 1. 홀짝
    # 2. 2step
    # 3. 2*?
    for i in range(N):
        st = road[2*i]
        ed = road[2*i+1]

    ##########################
    # 저장 방법
    # 1. ch1, ch2
    ch1 = [0] * 100
    ch2 = [0] * 100

    for i in range(N):
        if ch1[road[2*i]] == 0:
            ch1[road[2*i]] = road[2*i+1]
        else:
            ch2[road[2*1]] = road[2*i+1]

    # 2. 인접행렬 방식
    def DFS(v):
        global ans
        if v == 99:
            ans = 1
            return
        visited[v] = 1
        for w in rnage(100):
            if not visited[w] and adj_arr[v][w]:
                DFS(w)

    adj_arr = [[0] * 100 for _ in range(100)]
    for i in range(N):
        adj_arr[road[2*1]][road[2*i+1]] = 1
    visited = [0] * 100
    ans = 0

    # 3. 인접리스트 방식
    adj_list = [[] for _ in range(100)]
    for i in range(N):
        adj_list[road[2*i]].append(road[2*i+1])

    #