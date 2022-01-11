import sys
sys.stdin = open("input.txt")

def dfs(index):
    # 인덱스 범위 벗어나면 0
    if index > N + 1:
        return 0
    # 노드값을 알고있으면 바로 리턴
    if Tree[index]:
        return Tree[index]

    # 좌측, 우측 노드번호 구하기
    left = index * 2
    right = index * 2 + 1

    # 재귀로 좌측 value + 우측 value
    Tree[index] = dfs(left) + dfs(right)

    return Tree[index]

T = int(input())

for tc in range(1, T+1):
    # 노드개수 / 리프노드 개수 / 출력할 노드 번호
    N, M, L = map(int, input().split())
    Tree = [0 for _ in range(N + 2)]

    # input받은 리프노드의 값들 입력
    for i in range(M):
        node, value = map(int, input().split())

        Tree[node] = value

    answer = dfs(L)

    print('#{} {}'.format(tc, answer))