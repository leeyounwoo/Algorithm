import sys
sys.stdin = open('input.txt')

def inorder(node):
    if node != 0:
        inorder(tree[int(node)][1])  # 왼쪽 자식 방문
        print(tree[int(node)][0], end="")  # 부모 노드 방문
        inorder(tree[int(node)][2])  # 오른쪽 자식 방문


T = 10
for tc in range(1, T +1):
    N = int(input()) # 8
    tree = [[0 for _ in range(3)] for _ in range(N + 1)]  # left right parent
    print('#{}'.format(tc), end=' ')

    for i in range(1, N+1) :
        words = input().split()
        for j in range(len(words)-1):
            tree[i][j] = words[j+1]

    inorder(1)
    print()
