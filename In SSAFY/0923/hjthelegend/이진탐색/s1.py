import sys
sys.stdin = open('input.txt')

def build(idx):
    global count
    if idx <= n:
        build(idx*2)
        tree[idx] = count
        count += 1
        build(idx*2 + 1)

t = int(input())

for tc in range(1, t+1):
    n = int(input())

    # 이진 탐색 트리의 루트에 저장된 값
    # n//2번 노드에 저장된 값 출력

    # 중위순위(왼-나-오)를 하면 정렬된 형태
    tree = [0 for i in range(n + 1)]
    count = 1
    build(1)
    print(tree)
    print('#{} {} {}'.format(tc, tree[1], tree[n//2]))