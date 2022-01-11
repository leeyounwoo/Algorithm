import sys
sys.stdin = open('input.txt')

def inorder(node):
    global result

    if node:
        inorder(tree[node][0])
        result += alpha[node-1]
        inorder(tree[node][1])


for t in range(1, 11):
    V = int(input())

    tree = [[0 for _ in range(2)] for _ in range(V+1)] # l. r
    alpha = []
    for _ in range(V):
        temp = input().split()

        alpha.append(temp[1])

        if len(temp) >= 3:
            tree[int(temp[0])][0] = int(temp[2])

        if len(temp) >= 4:
            tree[int(temp[0])][1] = int(temp[3])

    result = ''
    inorder(1)

    print('#{} {}'.format(t, result))