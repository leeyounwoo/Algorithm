import sys
sys.stdin = open('input.txt')
# 중위순회
def inoreder(node):
    global count
    # N을 넘어가면 안됨
    if node <= N:
        inoreder(node*2)
        tree[node] = count
        count += 1
        inoreder(node*2+1)


for T in range(1, 1+int(input())):
    N = int(input())
    tree = [0 for _ in range(N+1)]
    count = 1
    inoreder(1)
    print('#{} {} {}'.format(T, tree[1], tree[N//2]))