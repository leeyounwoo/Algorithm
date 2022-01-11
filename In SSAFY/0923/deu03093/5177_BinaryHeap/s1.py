for T in range(1, 1+int(input())):
    N = int(input())
    tree = [0 for _ in range(N+1)]
    numbers = list(map(int, input().split()))
    for i in range(1, N+1):
        tree[i] = numbers[i-1]
        parent_node = i//2
        child_node = i
        # 루트노드의 번호가 1번이기 때문에 0이면 종료
        # 자식노드가 부모노드보다 더 큰 경우엔 순서 바꿔줌
        while parent_node != 0 and tree[parent_node] > tree[child_node]:
            tree[parent_node], tree[child_node] = tree[child_node], tree[parent_node]
            # 한단계씩 올라감
            child_node = parent_node
            parent_node = child_node // 2
    ans = 0
    last_node = N
    parent_node = last_node // 2
    while parent_node != 0:
        ans += tree[parent_node]
        parent_node //= 2
    print('#{} {}'.format(T, ans))