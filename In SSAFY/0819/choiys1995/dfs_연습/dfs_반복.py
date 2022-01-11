import sys
<<<<<<< HEAD
sys.stdin = open('input.txt')

def dfs(v):
    stack = []

    stack.append(v) # 시작 지점 스택에 삽입
    while stack:    # 순회 시작
        v = stack.pop() # 현재 방문하려는 노드

        if visited[v] == 0:
            visited[v] = 1 # 방문 표기
            print(v, end=' ') # 현재 방문한 노드 출력

            for w in range(1, V+1): # 인접 노드 순회
                if G[v][w] == 1 and visited[w] == 0: # 인접 노드중 갈 수 있는 곳이면
=======
sys.stdin = open("input.txt")

def dfs(v):
    stack = []
    stack.append(v)

    while stack:
        v = stack.pop()

        if visited[v] == 0:
            visited[v] = 1
            print(v, end = " ")
            for w in range(1, V+1):
                if G[v][w] == 1 and visited[w] == 0:
>>>>>>> 594c4091f9746ad09dd55cc5689632c610d27bfd
                    stack.append(w)

V, E = map(int, input().split())
temp = list(map(int, input().split()))

<<<<<<< HEAD
G = [[0 for _ in range(V+1)] for _ in range(V+1)] # 인접 행렬
visited = [0 for _ in range(V+1)]

for i in range(0, len(temp)-1, 2):
    G[temp[i]][temp[i+1]] = 1 # 인접한 노드 표기
    G[temp[i+1]][temp[i]] = 1 # 반대 방향도 표기

for i in range(V+1):
    for j in range(V+1):
        print(G[i][j], end=' ')
    print()

dfs(1) # 시작점(v)을 1로 설정
=======
G = [[0 for _ in range(V+1)] for _ in range(V+1)]
visited = [0 for _ in range(V+1)]

for i in range(0, len(temp)-1, 2):
    G[temp[i]][temp[i+1]] = 1 # 인접 노드
    G[temp[i+1]][temp[i]] = 1 # 반대 방향 (무방향 이므로)

for i in range(V+1):
    for j in range(V+1):
        print(G[i][j], end = " ")
    print()

dfs(1)
>>>>>>> 594c4091f9746ad09dd55cc5689632c610d27bfd
