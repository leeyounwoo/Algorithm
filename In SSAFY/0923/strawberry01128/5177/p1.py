import sys
sys.stdin = open('input.txt')

def postorderleft(node):
    # 왼 -> 오 -> 나
    #왼쪽
    if node*2 >= V:
        return
    if tree[node*2] < tree[node]:
        tree[node*2], tree[node] = tree[node], tree[node*2]
    if tree[node*2+1] < tree[node]:
        tree[node*2+1], tree[node] = tree[node], tree[node*2+1]
    postorderleft(node * 2)
    postorderleft(node * 2 + 1)

def postorderright(node):
    if node == 0:
        return
    # postorder(tree[])

T = int(input())
for tc in range(1,T+1):
    V = int(input())
    power_tree = [0]
    tree = power_tree + (list(map(int,input().split())))
    t = 0
    result = 0
    while True:
        if 2 ** t > V:
            break
        else:
            t += 1
    postorderleft(1)
    while V > 0:
        V = V // 2
        result += tree[V]
    print(result)