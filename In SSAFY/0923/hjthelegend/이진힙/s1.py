import sys
sys.stdin = open('input.txt')

def heap_sort():
    # idx // 2보다 작은지 확인해야함.
    idx = len(tree) - 1 # 노드 0은 없으니까
    if idx > 1:  # 이거 없으면 tree[0]과 스왑함
        while tree[idx] < tree[idx//2]: # if를 while로 바꿔주니 test_case 다 성공
            tree[idx], tree[idx//2] = tree[idx//2], tree[idx]
            idx //= 2

def total():
    result = 0
    idx = n // 2 # 제일 마지막 노드의 상위 노드
    while idx:
        result += tree[idx]
        idx //= 2
    return result

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    edges = list(map(int, input().split()))
    tree = [0] # 처음에 아무것도 없는 상태에서 시작하라 했음
    # 마지막 노드의 조상 노드 합 구하기

    # 정렬부터 해야됌
    for i in edges:
        tree.append(i)
        heap_sort()

    # 상위노드 합 구하기
    answer = total()
    print('#{} {}'.format(tc, answer))

