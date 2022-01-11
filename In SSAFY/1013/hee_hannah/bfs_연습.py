'''
7
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''

N = int(input())
edges = list(map(int, input().split()))

adj_list = { x: [] for x in range(1, N+1)}
for i in range(0, len(edges)-1, 2):
    s, e = edges[i], edges[i+1]
    adj_list[s].append(e)
    adj_list[e].append(s)

# BFS
s = 1
queue = [s]
# queue.pop(0) => O(n) 앞을 빼면 뒤에잇는걸 땡기는 과정이니까
# 오래걸리면 그냥 from collections import deque.. 얘는 바로 빼져서 O(1) 걸림
# 그치만 deque는 가운데에 있는 것 뺄때는 오래걸림
visited = [0] * (N + 1)
visited[s] = 1
while queue:
    v = queue.pop(0) # 1 을 본다면
    print(v, end=" => ")
    # 인접한 이웃 노드 탐색
    for u in adj_list[v]: # 1의 value 값
        if not visited[u]:
            queue.append(u)
            visited[u] = 1

