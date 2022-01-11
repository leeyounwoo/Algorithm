import sys
sys.stdin = open('input.txt')


def inorder(N, tree, node):
    if node > N:
        return

    global num
    inorder(N, tree, node*2)
    tree[node] = num
    num += 1
    inorder(N, tree, (node*2)+1)


num = 1
T = int(input())
for tc in range(1, T+1):
    num = 1
    N = int(input())
    tree = [0] * (N+1)
    inorder(N, tree, 1)
    result = ' '.join([str(tree[1]), str(tree[N//2])])
    print(f'#{tc} {result}')
