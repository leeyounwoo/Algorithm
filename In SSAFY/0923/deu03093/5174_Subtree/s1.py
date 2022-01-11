import sys
sys.stdin = open('input.txt')

def preorder(node):
    global cnt
    if node:
        cnt += 1
        for i in tree[node]:
            preorder(i)

for T in range(1, 1+int(input())):
    E, N = map(int, input().split())
    edges = list(map(int, input().split()))
    cnt = 0
    # 자식 노드 리스트
    tree = [[] for _ in range(E+2)]
    for i in range(0, len(edges)-1, 2):
        tree[edges[i]].append(edges[i+1])
    print(tree)
    preorder(N)
    print('#{} {}'.format(T, cnt))