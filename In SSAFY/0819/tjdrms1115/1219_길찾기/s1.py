import sys
sys.stdin = open('input.txt')


# 스택 클래스입니다.
class Stack:

    # 스택을 초기화합니다. 속도를 위해 고정 크기를 사용했습니다.
    def __init__(self):
        self.stack = [-1] * 100
        self.idx = -1

    # 스택이 비어있는지 검사하는 함수입니다.
    def is_empty(self):
        if self.idx == -1:
            return True
        return False

    # 스택 푸시
    def push(self, item):
        self.idx += 1
        self.stack[self.idx] = item

    # 스택 팝
    def pop(self):
        if self.idx == -1:
            return None
        item = self.stack[self.idx]
        self.stack[self.idx] = -1
        self.idx -= 1
        return item

    # 스택 맨 위의 값을 반환하는 함수입니다.
    def peek(self):
        return self.stack[self.idx]


# 깊이 우선 탐색 알고리즘을 구현했습니다.
def dfs(stack: Stack, V, E, graph, S, G):

    # 방문 여부를 저장할 리스트를 생성합니다.
    visited = [False for _ in range(V)]

    # 스택에 맨 처음 위치를 푸시하고 방문 리스트에 표시합니다.
    stack.push(S)
    visited[S] = True
    # 혹시나 시작점과 끝점이 같으면 바로 결과를 반환합니다.
    if S == G:
        return 1
    # 스택이 비어있지 않다면 탐색을 이어갑니다.
    while not stack.is_empty():
        # 스택 제일 위의 정점을 확인합니다.
        i = stack.peek()
        # 해당 정점에서 갈 수 있는 위치를 찾아봅니다.
        w = None
        for j in range(V):
            # 다른 정점으로 갈 수 있으면 해당하는 위치를 스택에 넣고 탐색을 즉시 종료합니다.
            if (graph[i][j] == 1) and (not visited[j]):
                w = j
                visited[j] = True
                stack.push(w)
                break
        # 다음 위치가 존재할 경우 탐색을 이어갑니다.
        while w:
            # 스택 제일 위의 정점을 확인합니다.
            i = stack.peek()
            # 정점이 도착점이라면 탐색을 종료합니다.
            if i == G:
                return 1
            # 해당 정점에서 갈 수 있는 위치를 찾아봅니다.
            w = None
            for j in range(V):
                # 다른 정점으로 갈 수 있으면 해당하는 위치를 스택에 넣고 탐색을 즉시 종료합니다.
                if (graph[i][j] == 1) and (not visited[j]):
                    w = j
                    visited[j] = True
                    stack.push(w)
                    break
        # 스택 맨 위의 정점에서 더 이상 갈 수 있는 곳이 없습니다.
        # 정점을 팝하고 이전 정점으로 돌아갑니다.
        stack.pop()
    # 도착점을 찾지 못했기 때문에 탐색 실패를 알립니다.
    return 0


# T = int(input())
T = 10

answer = []
for tc in range(1, T+1):
    # 스택을 초기화하고 그래프를 입력받습니다.
    stack = Stack()
    V = 100
    testcase, E = map(int, input().split())
    graph = [[0 for _ in range(V)] for _ in range(V)]
    input_seq = list(map(int, input().split()))
    for i in range(E):
        a = input_seq[i*2]
        b = input_seq[(i*2)+1]
        graph[a][b] = 1
    # 시작점과 끝점을 설정합니다.
    S, G = 0, 99

    # 깊이 우선 탐색을 수행합니다.
    result = dfs(stack, V, E, graph, S, G)

    # 결과를 출력합니다.
    answer.append(result)

for tc in range(1, T+1):
    print('#{} {}'.format(tc, answer[tc-1]))
