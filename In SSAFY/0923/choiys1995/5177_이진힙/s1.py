import sys
sys.stdin = open("input.txt")

def insert_heap(data):
    # heap에 값을 넣을때 마다 비교
    heap.append(data)
    index = len(heap) - 1
    # 루트노드는 부모가 없으니 index > 1 & 부모 노드 값 < 자식 노드 값인지
    while index > 1 and heap[index] < heap[index // 2]:
        # 부모 자식 값 교체
        heap[index], heap[index // 2] = heap[index // 2], heap[index]
        # 교체했는데 바뀐 부모가 조상보다 작을 수도 있다.
        index //= 2


def get_sum_heap():
    cnt = 0
    index = N // 2
    while index:
        cnt += heap[index]
        index //= 2
    return cnt


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    heap = [0]
    answer = 0
    for data in arr:
        insert_heap(data)
    answer = get_sum_heap()

    print('#{} {}'.format(tc, answer))