import sys
sys.stdin = open('input.txt')


def inorder(node):
    if node:
        inorder(G[node][2])
        print(G[node][0], end='')
        inorder(G[node][3])
# 3 R 6 7
# 4 O 8
# 5 T
for T in range(1, 11):
    N = int(input())
    G = [[0, 0, 0, 0] for _ in range(N+1)]  # char, parent, left, right
    for i in range(N):
        temp = list(input().split())  # now_idx, char, left, right,
        now_idx = int(temp[0])
        char = temp[1]
        # 그래프에서 현재 문자가 어떤건지 저장
        G[now_idx][0] = char

        # 현재 노드의 왼쪽 자식 노드가 몇번인지 저장
        if len(temp) >= 3:
            left_child = int(temp[2])
            G[now_idx][2] = left_child
            # 왼쪽 자식 노드의 부모 노드가 현재 노드임을 저장
            G[left_child][1] = now_idx
        if len(temp) == 4:
            right_child = int(temp[3])
            G[now_idx][3] = right_child
            G[right_child][1] = now_idx
    print(G)

    print('#{} '.format(T), end='')
    inorder(1)
    print()
