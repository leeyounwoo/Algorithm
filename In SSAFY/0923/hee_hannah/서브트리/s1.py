import sys
sys.stdin = open('input.txt')

t = int(input())

def inorder(node):
    global cnt
    # 왼 -> 나 -> 오
    if node == 0:
        return

    inorder(tree[node][1])
    # 프린트 대신 나 의 경우에는 개수 하나 더해주기
    cnt += 1
    inorder(tree[node][2])


for tc in range(1, t+1):
    print('#{}'.format(tc), end=" ")
    num_line, root = map(int, input().split())  # 간선의 개수, 최상단 루트
    edges = list(map(int, input().split()))
    # 간선의개수 +1 이 노드의 개수니까 num_line +2
    tree = [[0 for _ in range(3)] for _ in range(num_line+2)]
    cnt = 0 # 서브 트리 개수를 세자
    for i in range(0, len(edges)-1, 2):
        parent_node = edges[i]
        child_node = edges[i+1]

        # 왼쪽 자식이 비어있으면 넣고
        if not tree[parent_node][1]:
            tree[parent_node][1] = child_node
        # 왼쪽이 채워져 있으면 오른쪽에 넣기
        else:
            tree[parent_node][2] = child_node

        # 자식 노드의 부모 설정
        tree[child_node][0] = parent_node

    inorder(root)
    print(cnt)