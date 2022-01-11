import sys

sys.stdin = open('input.txt')
for T in range(1, int(input()) + 1):
    arr_size, kill_size = map(int, input().split())
    arr = []
    for _ in range(arr_size):
        arr.append(list(map(int, input().split())))

    ans = 0
    for i in range(arr_size - kill_size + 1):
        for j in range(arr_size - kill_size + 1):
            temp = 0
            for k_i in range(i, i + kill_size):
                for k_j in range(j, j + kill_size):
                    temp += arr[k_i][k_j]
            if ans < temp:
                ans = temp

    print('#{} {}'.format(T, ans))