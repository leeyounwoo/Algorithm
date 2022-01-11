import sys
sys.stdin = open('input.txt')


def inorder(node):
    global number
    if node == 0:
        return
    inorder(tree[node][1])
    if node <= N:
        tree[node].append(number)
        number += 1
    inorder(tree[node][2])


T = int(input())
for tc in range(T):
    N = int(input())
    tree = [[0]*3 for _ in range(N+2)]

    n = 1
    while True:
        tree[n][1] = n * 2
        tree[n][2] = n * 2 + 1

        tree[n*2][0] = n
        tree[n*2+1][0] = n
        if tree[n][1] >= N or tree[n][2] >= N:
            break
        n += 1

    number = 1
    inorder(1)
    print('#{} {} {}'.format(tc+1, tree[1][3], tree[N//2][3]))

