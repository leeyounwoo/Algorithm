import sys
sys.stdin = open('input.txt')

def selection_sort(arr):
    for i in range(len(arr) - 1):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[min_idx], arr[i] = arr[i], arr[min_idx]
    return arr

TC = int(input())

for tc in range(1, TC + 1):
    n = int(input())
    nums = list(map(int, input().split()))
    results = []
    nums = selection_sort(nums)

    while nums:
        results.append(nums.pop(-1))
        results.append(nums.pop(0))

    print(f"#{tc}", end=' ')
    for i in range(10):
        print(results[i], end=" ")
    print()
