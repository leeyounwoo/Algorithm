import sys
sys.stdin = open('input.txt')


def node_sum(node):
    if node > N:
        return 0

    if node in leaf_node_list:
        return tree[node]

    tree[node] = node_sum(node*2) + node_sum(node*2 + 1)
    return tree[node]


T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    tree = [0 for _ in range(N+1)]
    leaf_node_list = []

    for _ in range(M):
        leaf_node, num = map(int, input().split())
        leaf_node_list.append(leaf_node)
        tree[leaf_node] = num

    node_sum(L)
    print('#{} {}'.format(tc, tree[L]))
