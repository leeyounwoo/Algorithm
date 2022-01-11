import sys

sys.stdin = open('input.txt')

for T in range(1, 11):
    int(input())
    arr = []
    for _ in range(100):
        arr.append(list(map(int, input().split())))

    ans = -1
    width_list = []
    height_list = []
    cross_left = 0
    cross_right = 0
    for i in range(100):
        width_list.append(sum(arr[i]))
        height = 0
        cross_left += arr[i][i]
        cross_right += arr[99 - i][99 - i]
        for j in range(100):
            height += arr[j][i]
        height_list.append(height)

    ans = max(max(width_list), max(height_list), cross_right, cross_left)
    print('#{} {}'.format(T, ans))