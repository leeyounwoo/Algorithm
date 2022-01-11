import sys
sys.stdin = open('input.txt')


def calc(v):
    if len(tree[v]) == 2:
        return tree[v][1]
    else:
        L = calc(tree[v][2])
        R = calc(tree[v][3])

        if tree[v][1] == '+': return L+R
        elif tree[v][1] == '-': return L-R
        elif tree[v][1] == '*': return L*R
        elif tree[v][1] == '/': return L/R



for tc in range(10):
    N = int(input())
    tree = [0] * (N+1)

    for i in range(1, N+1):
        tem = input().split()

        tree[int(tem[0])] = tem

        if len(tem) == 4:
            tree[int(tem[0])][2] = int(tree[int(tem[0])][2])
            tree[int(tem[0])][3] = int(tree[int(tem[0])][3])
        else:
            tree[int(tem[0])][1] = int(tree[int(tem[0])][1])

    print('#{} {}'.format(tc+1, int(calc(1))))
