import sys
sys.stdin = open('input.txt')
def rotate(arr, n):
    new_arr = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            new_arr[i][j] = str(arr[n-j-1][i])
    return new_arr

T = int(input())
for tc in range(3):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    rotate_90 = [arr]

    for i in range(3):
        rotate_90.append(rotate(rotate_90[i], N))
    print('#{}'.format(tc + 1))
    for i in range(N):
        print(''.join(rotate_90[1][i]), ''.join(rotate_90[2][i]), ''.join(rotate_90[3][i]))