import sys

sys.stdin = open('input.txt')

'''
# 1. 어떻게 가져올 것인가
홀짝
2step range(0, len(road), 2)로 놓고 i와 i+1로 접근
2 * ? for i in range(N) -> 2 * i. 2*i + 1
# 2. 어떻게 저장할 것인가?
ch1, ch2 ch1=[0] * 100, ch2=[0]*100

for _ in range(1):
    tc, N = map(int, input().split())
    road = list(map(int, input().split()))
    
    # 3. 2*?
    for i in range(N):
        st = road[2*i]
        ed = road[2*i +1]
        print(st, ed)

    ############
    # 저장 방법
    # 1. ch1 ch2
    ch1 = [0] * 100
    ch2 = [0] * 100

    for i in range(N):
        if ch1[road[2 * i]] == 0:  # if 시작점 == 도착점
            ch1[road[2 * i]] = road[2 * i + 1]
        else:
            ch2[road[2 * i]] = road[2 * i + 1]
    # 인접행렬 방식
    adj_arr = [[0] * 100 for _ in range(100)]
    for i in range(N):
        adj_arr[road[2 * i][road[2 * i + 1]] = 1
    # 인접리스트 방식
    adj_list = [[] for _ in range(100)]
    for i in range(N):
        adj_list[road[2 * i]].append(road[2 * i + 1])
'''
for _ in range(10) :
    tc, N = map(int, input().split())
    road = list(map(int, input().split()))

    adj_list = [[] for _ in range(100)]
    for i in range(N):
        adj_list[road[2*i]].append(road[2*i+1])

    visited = [0] * 100
    ans = 0

    stack = [0]

    while stack : # 아니면 len(stack) = 0
        curr = stack.pop()
        if curr == 99:
            ans = 1
            break
        # 방문하지 않았으면

        # 방문을 했으면 건너가~~
        if visited[curr] : continue
        visited[curr] = 1

        for w in adj_list[curr]:
            if not visited[w]:
                stack.append(w)

    print('#{} {}'.format(tc, ans))
