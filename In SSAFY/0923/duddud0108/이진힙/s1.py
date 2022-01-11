import sys
sys.stdin = open('input.txt')

def binary_heap(n):
    heap.append(n)
    idx = len(heap) - 1
    while idx > 1:
        parent_idx = idx // 2
        if heap[parent_idx] > heap[idx]:
            heap[parent_idx], heap[idx] = heap[idx], heap[parent_idx]
        idx = parent_idx

def parent_sum(n):
    total = 0
    i = n
    while i > 1:
        i //= 2
        total += heap[i]
    return total


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))

    heap = [0]
    for i in nums:
        binary_heap(i)
    print('#{} {}'.format(tc,parent_sum(N)))