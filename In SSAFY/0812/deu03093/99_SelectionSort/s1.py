import random

arr = []
for i in range(10):
    arr.append((random.randrange(1, 10)))
print('초기 상태')
print(arr)

for i in range(len(arr) - 1):
    min_idx = i
    for j in range(i + 1, len(arr)):
        if arr[min_idx] > arr[j]:
            min_idx = j
    arr[i], arr[min_idx] = arr[min_idx], arr[i]

print('정렬 후')
print(arr)