import sys
sys.stdin = open('input.txt')

def bfs(v): # v : 출발 노드
    queue = []
    visited = [0] * (V+1) # V: 노드의 개수
    queue.append(v)
    count = 0 # 몇번만에 연결되는지 셀 변수
    while queue:
        new_v = queue.pop(0)
        if not visited[new_v]: # 방문한 적이 없다면
            visited[new_v] = 1 # 방문처리( == 현재 노드를 방문했다는 뜻)
            for nb in range(1, 1+V): # nb: 이웃 노드
                # 현재 노드(new_v)와 연결되어있고 (G[new_v][nb] == 1)
                # 다음에 방문할 노드 nb 가 방문한 적이 없다면(visited[nb] == 0)
                if G[new_v][nb] == 1 and visited[nb] == 0:
                    if nb == end: # 다음 노드가 도착점과 동일하다면
                        return count # 연결수 반환
                    else: # 도착점과 다르면
                        queue.append(nb)
                        count += 1

def bfs2(v): # v : 출발 노드
    queue = []
    visited = [0] * (V+1) # V: 노드의 개수
    queue.append(v)
    visited[v] = 1 # 1위치에 1표시
    while queue:
        new_v = queue.pop(0) # 1
        print(new_v)
        for nb in range(1, 1+V): # nb: 이웃 노드
            # 현재 노드(new_v)와 연결되어있고 (G[new_v][nb] == 1)
            # 다음에 방문할 노드 nb 가 방문한 적이 없다면(visited[nb] == 0)
            if G[new_v][nb] == 1 and visited[nb] == 0:
                if nb == end: # 다음 노드가 도착점과 동일하다면
                    return visited[new_v] + 1 # 연결수 반환
                else: # 도착점과 다르면
                    queue.append(nb)
                    visited[nb] = visited[new_v] + 1


T = int(input())
for tc in range(1, T+1):

    V, E = map(int, input().split())

    temp = [list(map(int, input().split())) for _ in range(E)]
    # print(temp) #[[1, 4], [1, 3], [2, 3], [2, 5], [4, 6]]
    G = [[0 for i in range(V + 1)] for j in range(V + 1)]
    start, end = map(int, input().split())
    # 인접 행렬
    for i in range(len(temp)):  # 입력
        G[temp[i][0]][temp[i][1]] = 1
        G[temp[i][1]][temp[i][0]] = 1  # 방향성이 없는 그래프이므로 양쪽으로 줌

    print('#{} {}'.format(tc, bfs(1)))

