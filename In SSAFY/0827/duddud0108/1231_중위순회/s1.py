import sys
sys.stdin = open('input.txt')

def inorder(node):
    if node != 0:
        inorder(tree[node][0])
        order.append(node)
        inorder(tree[node][1])

def print_tree():
    for i in range(len(tree)):
        print(i, tree[i][0], tree[i][1], tree[i][2])

for tc in range(1, 11):
    V = int(input())
    temp = [input().split() for _ in range(V)]
    tree = [[0 for _ in range(3)] for _ in range(V+1)]  # left, right, parent

    alpha = {}
    for item in temp:
        parent_node = int(item.pop(0))
        alpha[parent_node] = item.pop(0)

        i = 0
        while item:
            child_node = int(item.pop(0))
            tree[parent_node][i] = child_node
            tree[child_node][2] = parent_node
            i += 1

    order = []
    inorder(1)
    print('#{}'.format(tc), end=' ')
    for i in order:
        print(alpha[i], end='')
    print()