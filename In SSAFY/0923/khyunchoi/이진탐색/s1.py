import sys
sys.stdin = open('input.txt')


def inorder(node):
    if node == 0:
        return

    inorder(tree[node][1])
    arr.append(node)
    inorder(tree[node][2])


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = []
    tree = [[0 for _ in range(3)] for _ in range(N+1)]

    for i in range(1, N+1):
        tree[i][0] = i // 2
        if i * 2 <= N:
            tree[i][1] = i * 2
        if i * 2 + 1 <= N:
            tree[i][2] = i * 2 + 1

    inorder(1)
    a = arr.index(1) + 1
    b = arr.index(N//2) + 1
    print('#{} {} {}'.format(tc, a, b))
