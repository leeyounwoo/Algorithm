import sys
sys.stdin = open("input.txt")

def inorder(node):
    node = int(node)
    if node != 0:
        inorder(tree[node][0]) # 왼쪽 자식 방문
        print(word[node], end="")   # 부모 노드 방문
        inorder(tree[node][1])
T = 10
for tc in range(1, T+1):
    N = int(input())
    word = [0] * (N+1)
    tree = [[0 for _ in range(3)] for _ in range(N+1)]
    for i in range(1, N+1):
        string = list(input().split())
        char = string[1]
        word[i] = char
        string.remove(char)
        if len(string) == 2:
            tree[i][2] = string[0]  # 현재(부모) 노드
            tree[i][0] = string[1]  # 현재 노드의 자식이 될 노드
        elif len(string) == 3:
            tree[i][2] = string[0]  # 현재(부모) 노드
            tree[i][0] = string[1]  # 현재 노드의 자식이 될 노드
            tree[i][1] = string[2]
        else:
            tree[i][2] = string[0]

    print('#{}'.format(tc), end=" ")
    inorder(1)
    print()