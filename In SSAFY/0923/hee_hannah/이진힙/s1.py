'''
3
6
7 2 5 3 4 6
6
3 1 4 16 23 12
8
18 57 11 52 14 45 63 40
'''
import sys
sys.stdin = open('input.txt')

t = int(input())
for tc in range(1, t+1):
    print('#{}'.format(tc), end=" ")
    n = int(input())+1 # 7
    edges = list(map(int, input().split()))
    tree = [[0, 0]]
    j = 1
    for i in edges:
        tree.append([i, j])
        j += 1
    print(tree)
    for k in range(2, n): # (0) 1 2 3 4 5 6
        a = k//2 # 1 0, 2 1, 3,1, 
        if tree[k][0] < tree[a][0]:
            tree[k][0], tree[a][0] = tree[a][0], tree[k][0]
    print(tree)
    # 마지막 노드? n노드 7
    fin = 0
    while True:
        n = n//2 # 7 3 1 -> 6 3 1 
        if n == 1:
            fin += tree[n][0]
            break
        else:
            fin += tree[n][0]
    print(fin)