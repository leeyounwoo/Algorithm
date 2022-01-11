import sys
sys.stdin = open('input.txt')

# 부모가 항상 자식보다 작아야 해
# 안 그러면 스위치

def switch(i):
    # 만약 부모가 자식보다 크다면
    # child, parent = parent, child 스위치
    parent_i = parent[i]
    if parent_i == 0:
        return
    parent_num = tree[parent_i]
    child_num = tree[i]
    if parent_num > child_num :
        tree[parent_i], tree[i] = tree[i], tree[parent_i]
    switch(parent_i)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))

    tree = [0]*(N+1)
    parent = [0]*(N+1)
    for i in range(1, N+1):
        parent[i] = i // 2
        tree[i] = nums[i-1]

    for i in range(1, N+1):
        switch(i)



