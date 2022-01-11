'''
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''
def postorder(node):
    # 왼 -> 오 -> 나
    if node == 0:
        return

    postorder(tree[node][1])
    postorder(tree[node][2])
    print(node, end="=>")


def inorder(node):
    # 왼 -> 나 -> 오
    if node == 0:
        return

    inorder(tree[node][1])
    print(node, end="=>")
    inorder(tree[node][2])


def preorder(node):
    # 나 -> 왼 -> 오 순으로 순회
    if node == 0:
        return

    # 1. 나 방문
    print(node, end="=>")
    # 2. 왼쪽 방문 => tree[node][1]
    preorder(tree[node][1])
    # 3. 오른쪽 방문 => tree[node][2]
    preorder(tree[node][2])


V = int(input())
edges = list(map(int, input().split()))

# 트리 표현
tree = [[0 for _ in range(3)] for _ in range(V+1)]

for i in range(0, len(edges)-1, 2):
    parent_node = edges[i]
    child_node = edges[i+1]

    # 왼쪽 자식이 비어있으면 넣고
    if not tree[parent_node][1]:
        tree[parent_node][1] = child_node
    # 있으면 오른쪽에 넣기
    else:
        tree[parent_node][2] = child_node

    # 자식 노드의 부모 설정
    tree[child_node][0] = parent_node


print('전위순회 - preorder')
preorder(1)
print()

print('중위순회 - inorder')
inorder(1)
print()

print('후위순회 - postorder')
postorder(1)