import sys
sys.stdin = open("input.txt")

T = int(input())


def inorder(n):
    global number
    # 최대 노드 개수를 넘지 않도록
    if n <= N:
        # inorder (좌측 노드는 인덱스 2배)
        inorder(n * 2)

        # 값 넣었으면 증가시키기
        tree[n] = number
        number += 1

        # (우측 노드는 인덱스 2배 + 1)
        inorder(n * 2 + 1)


for tc in range(1, T + 1):
    N = int(input())

    tree = [0 for i in range(N + 1)]
    number = 1
    inorder(1)
    print('#{} {} {}'.format(tc, tree[1], tree[N // 2]))