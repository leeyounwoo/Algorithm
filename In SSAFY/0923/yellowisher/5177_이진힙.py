import sys
sys.stdin = open('input.txt')

def heap_sort(node):
    # 부모노드 찾기
    parent_node = node // 2
    if parent_node <= 0:
        # 부모노드에 값이 없으면 return
        return
    else:
        if tree[parent_node] > tree[node]:
            tree[node], tree[parent_node] = tree[parent_node], tree[node]
            heap_sort(parent_node)

T = int(input())
for tc in range(T):
    N = int(input())
    array = list(map(int, input().split()))
    tree = [0]

    cnt = 1
    for num in array:
        tree.append(num)

        heap_sort(cnt)
        cnt += 1

    result = 0
    while N > 0:
        N //= 2
        result += tree[N]
    # print(tree)
    print(f'#{tc + 1} {result}')