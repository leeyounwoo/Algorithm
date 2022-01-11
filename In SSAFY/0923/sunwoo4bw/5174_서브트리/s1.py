import sys
sys.stdin = open('input.txt')

def anyorder(node):
    global cnt
    if node == 0:
        return
    cnt += 1
    # 왼쪽 자식
    anyorder(tree[node][0])
    # 오른쪽 자식
    anyorder(tree[node][1])

T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))
    tree = [[0, 0] for _ in range(E+2)] # [[0, 0] [6, 0] [1, 5] [0, 0] [0, 0] [3, 0] [4, 0]]

    for i in range(0, len(arr), 2): # 부모자식 쌍
        p = arr[i] # 부모 2 2 1 5 6
        c = arr[i+1] # 자식 1 5 6 3 4
        # 왼쪽 자식이 비어있으면 넣고
        if not tree[p][0]:
            tree[p][0] = c
        # 있으면 오른쪽에 넣기
        else :
            tree[p][1] = c
    cnt = 0
    anyorder(N)
    print('#{} {}'.format(tc, cnt))

