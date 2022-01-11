'''
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''


def preorder(node):
    if node != 0:
        print(node, end=" ")
        preorder(tree[node][0])
        preorder(tree[node][1])


def print_tree():
    for i in range(len(tree)):
        print(tree[i][0], tree[i][1], tree[i][2])



V = int(input())
E = V - 1
temp = list(map(int, input().split()))
tree = [[0] * 3 for _ in range(V+1)]    # left, right, parent

for i in range(0, len(temp)-1, 2):
    parent_node = temp[i]  # 현재 부모 노드
    child_node = temp[i+1] # 현재 노드의 자식이 될 노드

    if not tree[parent_node][0]:
        tree[parent_node][0] = child_node
    else:
        tree[parent_node][1] = child_node

    tree[child_node][2] = parent_node
print_tree()
print('전위 순회 : ', end=" ")
preorder(1)
print()