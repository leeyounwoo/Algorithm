import sys
sys.stdin = open('input.txt')


def preorder(node):
    global count
    # 나 -> 왼 -> 오 순으로 순회
    if node == 0:
        return
    count += 1
    # 2. 왼쪽 방문 => tree[node][1]
    preorder(tree[node][1])
    # 3. 오른쪽 방문 => tree[node][2]
    preorder(tree[node][2])



T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    edges = list(map(int, input().split()))

    # 트리 표현
    tree = [[0 for _ in range(3)] for _ in range(E + 2)]

    for i in range(0, len(edges) - 1, 2):
        parent_node = edges[i]
        child_node = edges[i + 1]

        # 왼쪽 자식이 비어있으면 넣고
        if not tree[parent_node][1]:
            tree[parent_node][1] = child_node
        # 있으면 오른쪽에 넣기
        else:
            tree[parent_node][2] = child_node

        # 자식 노드의 부모 설정
        tree[child_node][0] = parent_node

    count = 0
    preorder(N)
    print('#{} {}'.format(tc, count))
