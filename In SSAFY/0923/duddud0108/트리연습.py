import sys
sys.stdin = open('input.txt')

def preorder(n):
    if n:
        # 1. 나 방문
        print(n, end=' ')
        # 2. 왼쪽 방문
        preorder(tree[n][1])
        # 3. 오른쪽 방문
        preorder(tree[n][2])

def inorder(n):
    if n:
        inorder(tree[n][1])
        print(n, end=' ')
        inorder(tree[n][2])

def postorder(n):
    if n:
        postorder(tree[n][1])
        postorder(tree[n][2])
        print(n, end=' ')

V = int(input())
edges = list(map(int, input().split()))

tree = [[0 for _ in range(3)] for _ in range(V+1)]

for i in range(0, len(edges)-1, 2):
    parent_node = edges[i]
    child_node = edges[i+1]

    # 왼쪽 자식이 비어있으면 넣고
    if tree[parent_node][1] == 0:
        tree[parent_node][1] = child_node
    # 있으면 오른쪽에 넣기
    else:
        tree[parent_node][2] = child_node

    # 자식 노드의 부모 설정
    tree[child_node][0] = parent_node

print('전위순회')
preorder(1)
print()
print('중위순회')
inorder(1)
print()
print('후위순회')
postorder(1)