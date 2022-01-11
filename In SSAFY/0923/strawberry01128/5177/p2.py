import sys
sys.stdin = open('input.txt')

def postorderleft(node):

    if node*2 > V:
        return
    if node*2 < len(tree):
        if tree[node*2] < tree[node]:
            tree[node*2], tree[node] = tree[node], tree[node*2]
    if node*2+1 < len(tree):
        if tree[node*2+1] < tree[node]:
            tree[node*2+1], tree[node] = tree[node], tree[node*2+1]
    postorderleft(node * 2)
    postorderleft(node * 2 + 1)


T = int(input())
for tc in range(1,T+1):
    V = int(input())
    result = 0
    tree = [0]
    power_tree = (list(map(int,input().split())))
    for _ in range(V):
        tree.append(power_tree.pop(0))
        postorderleft(1)

    while V > 0:
        V = V // 2
        result += tree[V]
    print('#{} {}'.format(tc,result))