import sys
sys.stdin = open('input.txt')

def counter(n):
    if n == 0:
        return
    global count
    count += 1
    counter(tree[n][1])
    counter(tree[n][2])

t = int(input())

for tc in range(1, t+1):
    e, n = map(int, input().split())
    edges = list(map(int, input().split()))
    tree = [[0 for _ in range(3)] for _ in range(e+2)]
    for i in range(0, len(edges)-1, 2): # 0 2 4 6 8
        parent = edges[i]
        child = edges[i+1]
        if not tree[parent][1]:
            tree[parent][1] = child

        else:
            tree[parent][2] = child

        tree[child][0] = parent
    count = 0
    counter(n)
    print('#{} {}'.format(tc, count))