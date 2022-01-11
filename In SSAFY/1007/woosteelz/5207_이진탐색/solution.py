def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    prev = None

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] > target:
            current = "right"
            high = mid - 1
        elif arr[mid] < target:
            current = "left"
            low = mid + 1
        if prev == current:
            return False
        prev = current
    return False


TC = int(input())
for tc in range(1, TC + 1):
    N, M = map(int, input().split())
    first = list(map(int, input().split()))
    second = list(map(int, input().split()))
    first.sort()
    answer = 0

    for b in second:
        if binary_search(first, b):
            answer += 1

    print(f"#{tc} {answer}")
