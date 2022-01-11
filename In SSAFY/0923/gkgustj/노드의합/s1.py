import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T+1):
    N, M, L = map(int, input().split())

    tree = [0 for _ in range(N+1)]

    for _ in range(M):
        idx, num = map(int, input().split())
        tree[idx] = num

    for i in range(N, 1, -1):
        tree[i//2] += tree[i]
    
    print('#{} {}'.format(t, tree[L]))