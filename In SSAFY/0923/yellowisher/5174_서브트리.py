import sys
sys.stdin = open('input.txt')

def preoder(node):
    global cnt
    if node == 0:
        return
    cnt += 1
    preoder(tree[node][1])
    preoder(tree[node][2])

T = int(input())
for tc in range(T):
    E, N = map(int, input().split())
    edges = list(map(int, input().split()))

    tree = [[0 for _ in range(3)] for _ in range(E + 2)]

    for i in range(0, len(edges)-1, 2):
        parent_node = edges[i]
        child_node = edges[i+1]

        if not tree[parent_node][1]:
            tree[parent_node][1] = child_node
        else:
            tree[parent_node][2] = child_node
        tree[child_node][0] = parent_node

    cnt = 0
    preoder(N)
    print(f"#{tc + 1} {cnt}")