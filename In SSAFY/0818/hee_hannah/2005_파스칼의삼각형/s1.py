import sys
sys.stdin = open('input.txt')

t = int(input())

for tc in range(1, t+1):
    print('#{}'.format(tc))
    a = int(input()) #4

    b = [[0]*a for _ in range(a)]
    for i in range(a): #0 1 2 3
        for j in range(a):
            if i == j or j == 0:
                b[i][j] = 1
            else:
                b[i][j] = b[i-1][j] + b[i-1][j-1]
    for k in range(len(b)): # 0 1 2 3
        c = b[k][:k+1]
        print(*c)







