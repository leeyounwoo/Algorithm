import sys
sys.stdin = open('input.txt')

def count(n):
    global cnt
    if n:
        cnt += 1
        count(tree[n][1])
        count(tree[n][2])

T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())

    edges = list(map(int, input().split()))
    tree = [[0 for _ in range(3)] for _ in range(E+2)]

    for i in range(0, len(edges)-1, 2):
        parent_node = edges[i]
        child_node = edges[i+1]

        if tree[parent_node][1] == 0:
            tree[parent_node][1] = child_node
        else:
            tree[parent_node][2] = child_node

        tree[child_node][0] = parent_node

    cnt = 0
    count(N)
    print('#{} {}'.format(tc, cnt))