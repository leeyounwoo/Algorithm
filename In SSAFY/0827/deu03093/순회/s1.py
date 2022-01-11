import sys
sys.stdin = open('input.txt')


def print_tree():
    for i in range(len(tree)):
        print(i, tree[i][0], tree[i][1], tree[i][2])


def preorder(node):
    if node != 0:
        print(node, end=' ')
        preorder(tree[node][0])
        preorder(tree[node][1])


def inorder(node):
    if node != 0:
        inorder(tree[node][0])
        print(node, end=' ')
        inorder(tree[node][1])

def postorder(node):
    if node != 0:
        postorder(tree[node][0])
        postorder(tree[node][1])
        print(node, end=' ')


V = int(input())
E = V - 1
temp = list(map(int, input().split()))

tree = [[0 for _ in range(3)] for _ in range(V+1)] # left, right, parent

for i in range(0, len(temp)-1, 2):
    parent_node = temp[i]   # 현재(부모) 노드
    child_node = temp[i+1]  # 현재 노드의 자식이 될 노드

    # 현재 노드의 자식을 왼쪽부터 채우기
    # 왼쪽에 없으면 넣고, 있으면 오른쪽에 채워넣음
    if not tree[parent_node][0]:
        tree[parent_node][0] = child_node
    else:
        tree[parent_node][1] = child_node

    tree[child_node][2] = parent_node

# print_tree()

print('전위 순회 : ', end='')
preorder(1)
print()

print('중위 순회 : ', end='')
inorder(1)
print()

print('후위 순회 : ', end='')
postorder(1)
print()