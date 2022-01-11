import sys
sys.stdin = open('input.txt')

def binarysearch(n):
    global num
    if n <= N:
        binarysearch(n*2)
        tree[n] = num
        num += 1
        binarysearch(n*2 + 1)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    tree = [0 for _ in range(N+1)]
    num = 1
    binarysearch(1)
    print('#{} {} {}'.format(tc, tree[1], tree[N//2]))