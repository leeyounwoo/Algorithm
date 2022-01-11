import sys
sys.stdin = open('input.txt')


def postorder(N, tree, node):
    if not isinstance(tree[node][1], str):
        return tree[node][1]

    a = postorder(N, tree, tree[node][2])
    b = postorder(N, tree, tree[node][3])

    if tree[node][1] == '+':
        return a + b
    elif tree[node][1] == '-':
        return a - b
    elif tree[node][1] == '*':
        return a * b
    elif tree[node][1] == '/':
        return a / b


# T = int(input())
T = 10

answer = []
for tc in range(1, T + 1):

    N = int(input())
    # parent, value, left, right
    tree = [[0, 0, 0, 0] for _ in range(N + 1)]
    for _ in range(N):
        seq = list(input().split())
        if len(seq) == 2:
            idx, val = seq
            idx = int(idx)
            val = int(val)
            tree[idx][1] = val
        else:
            idx, oper, left, right = seq
            idx = int(idx)
            left = int(left)
            right = int(right)
            tree[idx][1] = oper
            tree[idx][2] = left
            tree[idx][3] = right
            tree[left][0] = idx
            tree[right][0] = idx

    result = int(postorder(N, tree, 1))

    answer.append(result)

for tc in range(1, T + 1):
    print(f'#{tc} {answer[tc-1]}')