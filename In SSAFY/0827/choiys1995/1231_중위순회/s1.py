import sys
sys.stdin = open('input.txt')

def inorder(node):
    if node <= N:
        inorder(node*2)
        print(tree[node], end='')
        inorder(node*2+1)


for tc in range(1, 11):
    N = int(input())
    tree = [0] * (N+1)
    for i in range(N):
        arr = list(input().split())
        tree[i+1] = arr[1] # 이 트리는 노드 번호가 1부터 시작함


    print('#{}'.format(tc), end=' ')
    inorder(1)
    print()
