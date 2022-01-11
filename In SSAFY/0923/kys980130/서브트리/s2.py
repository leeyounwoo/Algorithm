import sys
sys.stdin = open('input.txt')
def preorder(node):

    if node == 0:
        return
    global cnt
    cnt += 1
    preorder(left[node])
    preorder(right[node])
T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    edges = list(map(int, input().split()))
    left = [0] * (E+2)
    right = [0] * (E+2)
    for i in range(0, len(edges)-1, 2):
        parent_node, child_node = edges[i], edges[i+1]
        if left[parent_node]:
            right[parent_node] = child_node
        else:
            left[parent_node] = child_node
    cnt = 0
    preorder(N)
    print('#{} {}'.format(tc, cnt))

