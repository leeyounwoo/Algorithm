import sys
sys.stdin = open('input.txt')

def inorder(node):
    # 왼 -> 나 -> 오
    if node == 0:
        return

    inorder(tree[node])
    print()
    inorder(tree[node])



T = int(input())
for tc in range(1,T+1):
    V = int(input())
    tree = [0 for _ in range(V)]
    print(tree)
