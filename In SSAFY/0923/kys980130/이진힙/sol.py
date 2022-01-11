import sys
sys.stdin = open('input.txt')
T = int(input())

def insert(num, child_idx):
    # ex) num: 7, idx: 1

    # 마지막 위치에 값을 넣고
    heap[child_idx] = num
    parent_idx = idx // 2

    # 부모를 계속 찾아가면서, 자식이 더 크면 바꾸기
    # 만약 루트 노드면 X
    while (child_idx != 1 and heap[parent_idx] > heap[child_idx]):
        heap[parent_idx], heap[child_idx] = heap[child_idx], heap[parent_idx]
        child_idx = parent_idx
        parent_idx = parent_idx // 2

for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    heap = [0] * (N+1) # 이진힙 저장할 리스트

    # heap 구축하는 부분
    idx = 0
    for num in nums:
        idx += 1
        insert(num, idx)

    # 마지막 노드의 조상 노드
    result = 0
    last_idx = len(heap) - 1
    while last_idx != 1:
        last_idx //= 2
        result += heap[last_idx]

    print(f'#{tc} {result}')
