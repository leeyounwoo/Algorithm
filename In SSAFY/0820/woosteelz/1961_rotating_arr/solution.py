import sys
sys.stdin = open('input.txt')

def rotate(arr, num):
    new_arr = [[0 for _ in range(num)] for _ in range(num)]
    for i in range(num):
        for j in range(num):
            new_arr[i][j] = str(arr[num-j-1][i])
    return new_arr

TC = int(input())
for tc in range(TC):
    num = int(input())
    origin_arr = [list(map(int, input().split())) for _ in range(num)]
    next_arr = [origin_arr]
    for i in range(3):
        next_arr.append(rotate(next_arr[i], num))
    print('#{}'.format(tc+1))
    for i in range(num):
        print(''.join(next_arr[1][i]), ''.join(next_arr[2][i]), ''.join(next_arr[3][i]))

