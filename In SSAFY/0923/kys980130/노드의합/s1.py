import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    tree = [0 for _ in range(N+1)]
    for i in range(M):
        node, num = map(int, input().split())
        tree[node] = num
    for j in range(N, 2, -1):
        tree[j//2] += tree[j]
    print('#{} {}'.format(tc, tree[L]))



