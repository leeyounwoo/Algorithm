import sys
sys.stdin = open('input.txt')


def inorder(node):
    global count

    if node <= N:
        inorder(2 * node)
        tree[node] = count
        count += 1
        inorder(2*node + 1)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    tree = [0 for _ in range(N + 1)]
    count = 1
    inorder(1)

    print('#{} {} {}'.format(tc, tree[1], tree[N//2]))
