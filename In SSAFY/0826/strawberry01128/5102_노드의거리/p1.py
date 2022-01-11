import sys
sys.stdin = open('input.txt')

def Google(S,G):
    global answer
    visited[S] = 1
    # S 부터 출발할거야 갈 수 있는곳으로가
    # 처음에 1넣으면 그다음 갈수있는곳 간다.
    # 그 다음 거기서도 갈 수 있는 곳으로가 (넓이우선탐색)
    # 그리고 내려갈때마다 answer += 1해
    # END만나면 꺼
    # if S == G:
    #     return answer
    #
    # for k in range(V+1):
    #     if box[S][k] == 1 :
    #         if visited[k] == 0:
    #             queue.append(k)
    #             answer += 1
    #             return Google(k,G)

    while queue:
        S = queue.pop(0)
        for k in range(V+1):
            if box[S][k] == 1:
                if visited[k] == 0:
                    queue.append(k)
                    visited[k] = visited[S] + 1

                    if k == G:
                        return visited[k] - 1
    return 0

T = int(input())
for tc in range(1,T+1):
    V, E = map(int, input().split())
    result = []
    answer= 0
    box = [[0]*(V+1) for _ in range(V+1)]
    visited = [0] * (V+1)
    for _ in range(E):
        result.append(list(map(int,input().split())))
    S, E = map(int, input().split())
    queue = [S]
    for i in result:
        box[i[0]][i[1]] = 1
        box[i[1]][i[0]] = 1
    print('#{} {}'.format(tc,Google(S,E)))