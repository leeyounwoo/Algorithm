import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    tree = [0] * (N+1)
    for _ in range(M):
        i, val = map(int, input().split())
        tree[i] = val
    for i in range(N, 0, -1):
        tree[i//2] += tree[i]
    result = tree[L]
    print(f'#{tc} {result}')
