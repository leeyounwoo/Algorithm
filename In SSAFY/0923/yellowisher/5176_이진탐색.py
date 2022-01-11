import sys
sys.stdin = open('input.txt')

def inorder(i):
    global cnt
    if i <= N:
        # 좌측
        inorder(2 * i)
        # 갈 수 없는 경우 값 넣고 cnt 증가
        tree[i] = cnt
        cnt += 1
        # 우측
        inorder(2 * i + 1)

T = int(input())
for tc in range(T):
    N = int(input())
    tree = [0 for _ in range(N + 1)]

    cnt = 1
    inorder(1)
    # print(f"#{tc + 1} {tree[1]} {tree[N // 2]}")
    print(tree)