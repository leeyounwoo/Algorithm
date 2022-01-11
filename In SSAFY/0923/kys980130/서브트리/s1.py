import sys
sys.stdin = open('input.txt')
def preorder(node):
    # 나 -> 왼 -> 오 순으로 순회
    global cnt
    if node == 0:
        return
    cnt += 1
    preorder(tree[node][1])
    preorder(tree[node][2])
T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    edges = list(map(int, input().split()))
    tree = [[0 for _ in range(3)] for _ in range(E+2)]
    cnt = 0
    for i in range(0, len(edges)-1, 2):
        parent_node = edges[i]
        child_node = edges[i+1]
        if not tree[parent_node][1]:
            tree[parent_node][1] = child_node
        else:
            tree[parent_node][2] = child_node
        tree[child_node][0] = parent_node

    cnt = 0
    preorder(N)
    print('#{} {}'.format(tc, cnt))