import sys
sys.stdin = open('input.txt')

for T in range(1, 1+int(input())):
    node_count, leaf_node_count, index = map(int, input().split())
    tree = [0 for _ in range(node_count + 1)]
    for _ in range(leaf_node_count):
        leaf_index, value = map(int, input().split())
        tree[leaf_index] = value
    # 마지막 노드부터 루트노드까지 반복
    # 부모 노드에 자식 노드 값을 더하면서 진행
    for i in range(node_count, 0, -1):
        now = i
        parent = i // 2
        tree[parent] += tree[now]
    print('#{} {}'.format(T, tree[index]))
