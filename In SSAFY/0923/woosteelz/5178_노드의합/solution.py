import sys
sys.stdin = open('0923/woosteelz/5178_노드의합/input.txt')

for tc in range(int(input())):
    N, M, L = map(int, input().split())
    tree = [0 for _ in range(N+1)]
    for _ in range(M):
        node, num = map(int, input().split())
        tree[node] = num

    for idx in range(N, 1, -1):
        if not idx % 2 and not tree[idx//2]:
            if idx + 1 <= N:
                tree[idx//2] = tree[idx] + tree[idx+1]
            else:
                tree[idx // 2] = tree[idx]

    print(f'#{tc+1} {tree[L]}')
