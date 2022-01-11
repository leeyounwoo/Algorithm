import sys

sys.stdin = open('input.txt')

for T in range(1, int(input()) + 1):
    arr_size = int(input())
    arr = list(map(int, input().split()))
    for i in range(len(arr) - 1):
        # 바꿀 인덱스
        change_idx = i
        # 홀수 번째는 작은거
        if i % 2:
            for j in range(i + 1, len(arr)):
                if arr[change_idx] > arr[j]:
                    change_idx = j
            arr[i], arr[change_idx] = arr[change_idx], arr[i]
        # 짝수 번째는 큰거
        else:
            for j in range(i + 1, len(arr)):
                if arr[change_idx] < arr[j]:
                    change_idx = j
            arr[i], arr[change_idx] = arr[change_idx], arr[i]
    print('#{}'.format(T), end=' ')
    for i in range(10):
        print(arr[i], end=' ')
    print()