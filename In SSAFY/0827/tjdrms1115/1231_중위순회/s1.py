import sys
sys.stdin = open('input.txt')


def inorder(node):
    global result
    if node != 0:
        inorder(tree[node][1])
        result += tree[node][0]
        inorder(tree[node][2])


# T = int(input())
T = 10

answer = []
for tc in range(1, T+1):
    N = int(input())
    # tree component: letter, left, right, parent
    tree = [[0 for _ in range(4)] for _ in range(N+1)]
    for _ in range(N):
        seq = list(input().split())
        parent = int(seq[0])
        letter = seq[1]
        tree[parent][0] = letter
        if len(seq) >= 3:
            left = int(seq[2])
            tree[parent][1] = left
            tree[left][3] = parent
        if len(seq) >= 4:
            right = int(seq[3])
            tree[parent][2] = right
            tree[right][3] = parent

    result = ''
    inorder(1)

    answer.append(result)

for tc in range(1, T+1):
    print('#{} {}'.format(tc, answer[tc-1]))
