import sys
sys.stdin=open('input.txt')


def preorder(node):
    global count
    if node == 0:
        return
    count += 1
    preorder(tree[node][1])

    preorder(tree[node][2])


T = int(input())
for tc in range(1,T+1):
    V,E = map(int,input().split())

    edges = list(map(int, input().split()))
    # 트리 표현
    tree = [[0 for _ in range(4)] for _ in range(V+2)]

    count = 0
    for i in range(0, len(edges)-1, 2):
        parent_node = edges[i]
        child_node = edges[i+1]

        if not tree[parent_node][1]:
            tree[parent_node][1] = child_node

        else:
            tree[parent_node][2] = child_node

        tree[child_node][0] = parent_node
    preorder(E)
    print('#{} {}'.format(tc,count))