import sys
sys.stdin = open("input.txt")


# 중위탐색
def inorder(node_idx):
    global cnt            # cnt 값 global 변수로 선언하여 사용

    if 1 <= node_idx <= N:   # 왼쪽 서브 트리의 루트 노드의 값 < 현재 노드의 값 < 오른쪽 서브트리의 루트 노드의 값
        left = node_idx * 2  # 왼쪽
        if 0 < left < N + 1:
            inorder(left)
        tree[node_idx] = cnt
        cnt += 1
        right = node_idx * 2 + 1  # 오른쪽

        if 0 < right < N + 1:
            inorder(right)


T = int(input())
for tc in range(1, T + 1):
    # N: 노드의 개수
    N = int(input())

    # 값을 저장할 트리 배열
    tree = [0] * (N + 1)

    cnt = 1
    inorder(1)  # 트리에 저장할 값, 1부터 시작
    print('#{} {} {}'.format(tc, tree[1], tree[N // 2]))
