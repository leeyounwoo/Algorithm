import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(T):
    N = int(input())
    arr = list(map(int, input().split()))

    for i in range(0, N - 1, 2):
        # 큰 값 정렬
        max_num = i
        for j in range(i + 1, N):
            if arr[max_num] < arr[j]:
                max_num = j
        arr[i], arr[max_num] = arr[max_num], arr[i]

        # 작은 값 정렬
        min_num = i + 1
        for k in range(i + 2, N):
            if arr[min_num] > arr[k]:
                min_num = k
        arr[i + 1], arr[min_num] = arr[min_num], arr[i + 1]

    # 출력 부분
    print("#{}".format(tc+1), end = " ")
    for out in range(10):
        print(arr[out], end = " ")
    print()