import sys
sys.stdin = open('input.txt')


def inorder(node):
    if node != 0:
        inorder(tree[node][0])
        print(tree[node][2], end='')
        inorder(tree[node][1])

T = 10
for tc in range(1, T+1):
    N = int(input())
    tree = [[0 for _ in range(3)] for _ in range(N+1)]
    for i in range(1, N+1):
        parent_node, node_char, *child_node = input().split()

        if len(child_node) == 2:
            tree[int(parent_node)][0] = int(child_node[0])
            tree[int(parent_node)][1] = int(child_node[1])
        elif len(child_node) == 1:
            tree[int(parent_node)][0] = int(child_node[0])

        tree[int(parent_node)][2] = node_char

    print('#{} '.format(tc), end='')
    inorder(1)
    print()