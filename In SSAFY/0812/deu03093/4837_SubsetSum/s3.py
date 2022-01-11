import sys

sys.stdin = open('input.txt')

for T in range(1, int(input()) + 1):
    ele_count, ele_sum = map(int, input().split())
    arr = [i for i in range(1, 13)]
    n = len(arr)

    ans = 0
    for i in range(1 << n):
        temp = []
        for j in range(n):
            if i & (1 << j):
                temp.append(arr[j])
        if len(temp) == ele_count:
            temp_sum = 0
            for k in range(len(temp)):
                temp_sum += temp[k]
            if temp_sum == ele_sum:
                ans += 1

    print('#{} {}'.format(T, ans))