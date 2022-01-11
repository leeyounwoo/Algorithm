import sys
sys.stdin = open('input.txt')

# 정점이 숫자 - 정점번호와 해당 양의 정수가 주어짐
# 정점이 연산자 - 정점번호, 연산자, 왼자번, 오자번
for tc in range(1, 11):
    N = int(input())  # 정점의 개수
    tree = [[0] * 3 for _ in range(N + 1)]
    for _ in range(N):
        data = list(map(str, input().split()))
        if len(data) == 2:  # 숫자만 있다는 것
            # data[0]: 정점 번호-> tree 인덱스
            tree[int(data[0])][1] = int(data[1])
        elif len(data) == 4:  # has 2 children
            tree[int(data[0])][1] = data[1] # 연산자
            tree[int(data[0])][0] = int(data[2])  # 왼자
            tree[int(data[0])][2] = int(data[3])  # 오자

    # print(tree)
    # [[0, 0, 0], [2, '-', 3], [4, '-', 5], [0, 10, 0], [0, 88, 0], [0, 65, 0]]
    # [[0, 0, 0], [2, '-', 3], [4, 23, 5], [0, 10, 0], [0, 88, 0], [0, 65, 0]]
    # [[0, 0, 0], [2, 13, 3], [4, 23, 5], [0, 10, 0], [0, 88, 0], [0, 65, 0]]

    for node in tree[::-1]: # [4, '-', 5]  [2, '-', 3]
        left = tree[node[0]][1] # 88 23
        right = tree[node[2]][1] # 65 10
        # node[1] 연산자 확인
        if node[1] == '+':
            node[1] = left + right
        elif node[1] == '-':
            node[1] = left - right
        elif node[1] == '*':
            node[1] = left * right
        elif node[1] == '/':
            node[1] = left // right

    # print(tree)
    # [[0, 0, 0], [2, 13, 3], [4, 23, 5], [0, 10, 0], [0, 88, 0], [0, 65, 0]]

    print('#{} {}'.format(tc, tree[1][1]))