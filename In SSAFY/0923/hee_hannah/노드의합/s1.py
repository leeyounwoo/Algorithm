import sys
sys.stdin = open('input.txt')

t = int(input())
for tc in range(1, t+1):
    print('#{}'.format(tc), end=" ")
    node_num, leaf_num, ans = map(int, input().split())
    tree = [0]*(node_num+1)

    for i in range(node_num-leaf_num+1, node_num+1):
        leaf_node, num = map(int, input().split())
        tree[leaf_node] = num
    print(tree)
    # 0 1 2 3 4 5
    # 0 0 0 3 1 2
    # 0 6 3 3 1 2
    #node_num+1 = 6
    for j in range(node_num-1, 1, -2):
        # 2 ~ 5   2 4
        a = j//2
        tree[a] = tree[j]+tree[j+1]
    print(tree)

