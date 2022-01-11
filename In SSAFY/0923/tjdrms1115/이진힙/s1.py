import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    tree = [0] * (N+1)
    numbers = list(map(int, input().split()))
    for i in range(1, N+1):
        num = numbers[i-1]
        tree[i] = num
        idx = i
        while tree[idx//2] > tree[idx]:
            tree[idx // 2], tree[idx] = tree[idx], tree[idx//2]
            idx //= 2

    idx = N // 2
    result = 0
    while idx > 0:
        result += tree[idx]
        idx //= 2

    print(f'#{tc} {result}')
