import sys
sys.stdin = open('input.txt')

def inorder(node):
    if node != 0:
        inorder(tree[int(node)][2]) # 왼쪽 자식 방문
        print(tree[int(node)][1], end="") # 부모 노드 방문
        inorder(tree[int(node)][3]) # 오른쪽 자식 방문

for tc in range(1,11):
    T = int(input())
    words = []
    for _ in range(T):
        words.append(list(map(str, input().split())))
    tree = [[0 for _ in range(4)] for _ in range(T + 1)]  # 부모노드, 알파벳, 자식노드1, 자식노드2
    for j in range(T):
        for i in range(len(words[j])):
            if words[j][i]:
                tree[j+1][i] = words[j][i]
            else:
                continue
    print('#{}'.format(tc),end=" ")
    inorder(1)
    print()