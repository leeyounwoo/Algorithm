import sys
sys.stdin = open('input.txt')

T = int(input())

def node_num(node):
    global cnt

    if node == 0:
        return
    cnt += 1
    node_num(tree[node][1])
    node_num(tree[node][2])


for tc in range(1, T+1):
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))
    tree = [[0 for _ in range(3)] for _ in range(E + 2)]

    for i in range(0, len(arr)-1, 2):
        parent, child = arr[i], arr[i + 1]
        # 왼쪽 노드 비었으면
        if not tree[parent][1]:
            tree[parent][1] = child
        # 아니라면
        else:
            tree[parent][2] = child

        tree[child][0] = parent

    cnt = 0
    node_num(N)
    print("#{} {}".format(tc, cnt))