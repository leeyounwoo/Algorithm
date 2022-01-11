import sys
sys.stdin = open('input.txt')

def node_hap(node):
    # 부모 노드 찾기
    parent_node = node // 2
    # parent_node가 0보다 작으면 return
    if parent_node <= 0:
        return
    else:
        # 부모 노드에 현재 노드의 값을 더해줌
        tree[parent_node] += tree[node]

T = int(input())
for tc in range(T):
    # 노드 개수 / 리프노드 개수 / 출력할 노드 번호
    N, M, L = map(int, input().split())
    # tree 배열 초기화
    tree = [0] * (N + 1)
    for _ in range(M):
        a, b = map(int, input().split()) # a는 노드 번호, b는 값
        tree[a] = b

    for i in range(N, 0, -1): # 가장 마지막 leaf node 저장 값부터 1씩 감소
        node_hap(i)

    print(f'#{tc + 1} {tree[L]}')
    # print(tree)