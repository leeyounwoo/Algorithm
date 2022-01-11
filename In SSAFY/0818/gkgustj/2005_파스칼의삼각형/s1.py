import sys

sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T+1):
    N = int(input())

    pascal = []
    for n in range(1, N+1):
        temp = [0]*n
        for i in range(n):
            if i == 0:
                temp[i] = 1
            elif i == n-1:
                temp[i] = 1
            else:
                temp[i] = pascal[n-2][i-1] + pascal[n-2][i]
        pascal.append(temp)

    print('#{}'.format(t))
    for row in pascal:
        print(*row)