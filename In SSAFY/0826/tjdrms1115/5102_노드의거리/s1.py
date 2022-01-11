import sys
sys.stdin = open('input.txt')


# 노드 간의 거리를 찾는 함수입니다.
def bfs(V, edges, start, goal):
    # 시작 노드와의 거리를 저장할 변수입니다.
    distance = 0
    # 방문 여부를 확인할 리스트입니다.
    visited = [0] * (V+1)
    # 큐로 사용할 리스트입니다. 시작값을 넣고 시작합니다.
    q = []
    q.append(start)
    # bfs 탐색입니다.
    while q:
        # 현재 큐에 저장되어 있는 만큼만 경로 찾기를 반복합니다.
        # while문 반복 한 번에 들어가는 노드들은
        # 같은 거리를 공유합니다.
        cur_item_num = len(q)
        for _ in range(cur_item_num):
            # 큐에 저장된 노드를 얻습니다.
            v = q.pop(0)
            # 방문하지 않았다면, 방문표시를 하고 다음 노드를 찾습니다.
            if not visited[v]:
                visited[v] = 1
                # 도착지에 다다르면 거리를 반환하고 함수를 종료합니다.
                if v == goal:
                    return distance
                for w in edges[v]:
                    if not visited[w]:
                        q.append(w)
        distance += 1
    # 큐가 빌 때까지 반환을 못했으면
    # 연결된 길이 없다는 의미이므로 0을 반환합니다.
    return 0


# 테스트 케이스의 개수를 입력받습니다.
T = int(input())

# 테스트 케이스만큼 코드를 실행하고 결과를 저장합니다.
answer = []
for tc in range(1, T+1):

    # 입력값을 받고, 초기값들을 설정합니다.
    V, E = map(int, input().split())
    edges = [[] for _ in range(V+1)]
    for _ in range(E):
        v, w = map(int, input().split())
        edges[v].append(w)
        edges[w].append(v)
    S, G = map(int, input().split())

    # bfs를 통해 길을 찾고 노드의 거리를 반환합니다.
    result = bfs(V, edges, S, G)
    # 결과를 출력합니다.
    answer.append(result)

for tc in range(1, T+1):
    print('#{} {}'.format(tc, answer[tc-1]))
