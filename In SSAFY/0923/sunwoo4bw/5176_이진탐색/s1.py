import sys
sys.stdin = open('input.txt')

# 중위로 풀기 -> 정렬된 형태로 값 출력
# 완전 이진 트리 -> 1부터 차례대로 번호 부여
# 어떤 순서대로 값을 넣으면 될지 생각해보기

# 루트에 저장된 값, N//2 번 노드에 저장된 값
# def inorder(node):
#     # 왼 -> 나 -> 오
#     if node == 0:
#         return
#
#     inorder(tree[node][1])
#     print(node, end="=>")
#     inorder(tree[node][2])

T = int(input())
for tc in range(1, T +1):
    N = int(input())
    tree = [[0,0] for _ in range(N+1)]
    # [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]

    # for i in range(1, N+1): #
    #     if i

    print('#{} {} {}'.format(tc, (N//2)+1, tree))

