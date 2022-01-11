import sys
sys.stdin = open('input.txt')

def node_sum(tree):
    idx = len(tree)-1
    while idx > 1:
        tree[idx//2] += tree[idx]
        idx -= 1


T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    tree = [0 for _ in range(N+1)]
    for _ in range(M):
        n, k = map(int, input().split())
        tree[n] = k
    node_sum(tree)
    print('#{} {}'.format(tc, tree[L]))