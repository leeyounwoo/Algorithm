import sys
sys.stdin = open('input.txt')


def inorder(x):
    if x <= N:
        inorder(x*2)  # 왼쪽 자식 방문
        print(node[x], end="")    # 부모 노드 방문
        inorder(x*2+1)  # 오른쪽 자식 방문


for tc in range(1, 11):
    N = int(input())
    node = [0] * (N+1)

    for i in range(N):
        temp = list(input().split())
        node[i+1] = temp[1]

    print('#{}'.format(tc), end=' ')
    inorder(1)
    print()

