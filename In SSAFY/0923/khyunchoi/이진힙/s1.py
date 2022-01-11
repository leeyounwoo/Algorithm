import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    vertexes = list(map(int, input().split()))
    tree = [[0 for _ in range(4)]]

    for vertex in vertexes:
        tree.append([vertex, 0, 0, 0])

        idx = len(tree) - 1
        # 부모 등록
        tree[idx][1] = tree[idx//2][0]
        # 자식 등록
        if idx != 1:
            if not tree[idx//2][2]:
                tree[idx//2][2] = vertex
            else:
                tree[idx//2][3] = vertex

        # 재배치
        while tree[idx][0] < tree[idx//2][0]:
            parent_vertex = tree[idx//2][0]
            for i in range(len(tree)):
                for j in range(4):
                    if tree[i][j] == parent_vertex:
                        tree[i][j] = vertex
                    elif tree[i][j] == vertex:
                        tree[i][j] = parent_vertex
            idx = idx // 2

        # 망한코드
        # if tree[idx][0] < tree[idx//2][0]:
        #     tree[idx][0], tree[idx//2][0] = tree[idx//2][0], tree[idx][0]
        #
        #     child_idx = tree[idx//2].index(vertex)
        #     another_idx = 2
        #     if child_idx == 2:
        #         another_idx = 3
        #
        #     tree[idx//2][child_idx], tree[idx][1] = tree[idx][1], tree[idx//2][child_idx]
        #
        #     if tree[idx//2][1]:
        #         if (idx//2) % 2 == 0:
        #             tree[(idx//2)//2][2] = tree[idx//2][0]
        #         else:
        #             tree[(idx//2)//2][3] = tree[idx//2][0]
        #
        #     if tree[idx//2][another_idx]:
        #         pass

    result = 0
    node = len(tree) - 1

    while node:
        result += tree[node][1]
        node //= 2

    print('#{} {}'.format(tc, result))
