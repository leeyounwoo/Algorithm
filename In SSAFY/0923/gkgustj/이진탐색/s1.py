import sys
sys.stdin = open('input.txt')

def inorder(node):
    # 왼 - 나 - 오
    if node <= N:
        inorder(node*2)
        tree.append(temp[node])
        inorder(node*2 + 1)


T = int(input())

for t in range(1, T+1):
    N = int(input())
    temp = [i for i in range(N+1)]
    # print(temp)

    tree = []
    inorder(1)
    # print(tree)

    ans1 = temp[tree.index(1)+1]
    ans2 = temp[tree.index(N//2)+1]

    print('#{} {} {}'.format(t, ans1, ans2))