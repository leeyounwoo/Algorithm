def bfs(queue):
    count = 1
    while queue:   # 큐 하나 생성
        second_queue = []  #2번째 큐생성
        while queue:
            index = queue.pop()
            for i in node[index]:
                if visited[i]: continue  # 방문했던곳은 pass
                if i == end:  # 목적지 도달 = 카운트
                    return count
                # 위의 조건에 걸리지 않는다면 두번재 큐에 추가한다.
                second_queue.append(i)
                # 방문처리를 한다.
                visited[i] = 1
        # 모든 큐가 비었다면 카운트를 증가시킨다.
        count += 1
        # 큐를 교체한다.
        queue = second_queue
    # 여기까지 왔다면 목적지까지 도착할 수 없다.
    return 0

import sys
sys.stdin = open('input.txt')

for t in range(1, int(input()) + 1):
    # V개의 노드, E개의 간선
    V, E = map(int, input().split())
    # 리스트를 이용한 간선 표시
    node = [[] for _ in range(V + 1)]
    # 방문여부
    visited = [0 for _ in range(V + 1)]
    # 데이터 편집
    for i in range(E):
        a, b = map(int, input().split())
        node[a].append(b)
        node[b].append(a)
    # 시작노드와 끝나는 노드 저장
    start, end = map(int, input().split())
    # 시작노드 방문처리
    visited[start] = 1
    # bfs 돌리기
    print('#{} {}'.format(t, bfs([start])))