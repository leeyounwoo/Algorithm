import sys
sys.stdin = open('input.txt')




def inorder(node):
    if node != 0:
        inorder(tree[node][0]) #
        print(node, end=' ')
        inorder(tree[node][1])

for tc in range(10):
    V = int(input())
    E = V-1

    temp = list(map(int, input().split()))

    tree = [[0 for _ in range(3)] for _ in range(V+1)]  # left, right, parent

    for i in range(0, len(temp)-1, 2):  # len(temp)-1인 이유는 11까지만 돌릴 것이기 때문
        parent_node = temp[i]   # 현재(부모) 노드
        child_node = temp[i+1]  # 현재 노드의 자식이 될 노드

        # 현재 노드의 자식을 왼쪽부터 채우기
        # 왼쪽에 없으면 넣고, 있으면 오른쪽에 채워넣음
        if not tree[parent_node][0]:
            tree[parent_node][0] = child_node
        else:
            tree[parent_node][1] = child_node

        tree[child_node][2] = parent_node
        print('#{} {}'.format(tc+1, inorder(V)))