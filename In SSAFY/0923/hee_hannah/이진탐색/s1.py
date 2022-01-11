'''
3
6
8
15
'''

import sys
sys.stdin = open('input.txt')

def inorder(node):
    # 왼 -> 나 -> 오
    if node == 0:
        return

    inorder(tree[node][1])
    print(node, end="=>")
    inorder(tree[node][2])


t = int(input())
for tc in range(1, t+1): # 루트값, n//2노드 값 출력...
    print('#{}'.format(tc),end=" ")
    n = int(input())
    tree = [0 for _ in range(n+1)]
    tree[1] = n//2+1
    print('{} {}'.format(tree[1],tree[n//2]))