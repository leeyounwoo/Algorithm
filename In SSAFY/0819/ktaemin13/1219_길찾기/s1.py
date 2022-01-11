import sys
sys.stdin = open('input.txt')

def dfs(v):
    stack = [v]

    while stack:
        v = stack.pop()

        if visited[v] == 0:
            visited[v] = 1

            for w in range(0, V+1):
                if G[v][w] == 1 and visited[w] == 0:  # 인접 노드 중 갈 수 있는 곳이라면
                    if w == V:
                        return 1
                    else:
                        stack.append(w)
    return 0

for tc in range(10):

    T, E = map(int, (input().split()))  # tc, E(가지 수) 입력
    temp = list(map(int, input().split()))  # 리스트 받아와서 저장
    s_temp = sorted(temp)  # V를 구하기 위해 정렬
    V = s_temp[-2] + 1  # 맨 마지막은 도착(99)이니 그 앞의 수를 확인하여 +1 하고(99포함) 노드에 저장

    G = [[0 for _ in range(V + 1)] for _ in range(V + 1)]  # 인접행렬 생성
    visited = [0 for _ in range(V + 1)]  # 방명록 생성

    for i in range(0, len(temp) - 1, 2):  # 인접한 노드 그리기
        if temp[i + 1] == 99:
            temp[i + 1] = V
            G[temp[i]][temp[i + 1]] = 1
        else:
            G[temp[i]][temp[i + 1]] = 1

    print('#{} {}'.format(tc+1, dfs(0)))