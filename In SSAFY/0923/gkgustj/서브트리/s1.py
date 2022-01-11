import sys
sys.stdin = open('input.txt')

def subtree(node):
    global cnt

    if node:
        cnt += 1
        subtree(tree[node][0])
        subtree(tree[node][1])


T = int(input())

for t in range(1, T+1):
    E, N = map(int, input().split())
    temp = list(map(int, input().split()))

    tree = [[0]*2 for _ in range(E+2)]
    
    for i in range(0, len(temp)-1, 2):
        if not tree[temp[i]][0]:
            tree[temp[i]][0] = temp[i+1]
        else:
            tree[temp[i]][1] = temp[i+1]
    
    cnt = 0
    subtree(N)

    print('#{} {}'.format(t, cnt))