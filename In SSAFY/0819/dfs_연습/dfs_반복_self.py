import sys
sys.stdin = open('input.txt')

def dfs(v):
    stack = []                   # 스택 초기화
    stack.append(v)              # 스택에 시작지점 생성

    while stack:                 # 순회 시작
        v = stack.pop()         # 시작 지점 꺼내옴

        if visited[v] == 0:      # 만약 방문한 곳이 아니라면,
            visited[v] = 1       # 방문 표시
            print(v, end=' ')    # 방문 노드 출력

            for w in range(1, V+1):                   
                if G[v][w] == 1 and visited[w] == 0:  # 방문 가능한 곳이고 방문한 적이 없다면,
                    stack.append(w)                   # stack에 추가

V, E = map(int, (input().split()))                  # 노드와 가지 수 받아옴
temp = list(map(int, input().split()))              # 그래프 받아옴

G = [[0 for _ in range(V+1)] for _ in range(V+1)]   # 인접 행렬 생성
visited = [0 for _ in range(V+1)]                   # 방문 여부 리스트 생성

for i in range(0, len(temp)-1, 2):
    G[temp[i]][temp[i+1]] = 1                       # 경로 생성
    G[temp[i+1]][temp[i]] = 1                       # 무방향일 경우 생성

for i in range(V+1):                                # 인접 행렬 출력 테스트
    for j in range(V+1):
        print(G[i][j], end=' ')
    print()

dfs(1)                                              # 시작 지점 설정