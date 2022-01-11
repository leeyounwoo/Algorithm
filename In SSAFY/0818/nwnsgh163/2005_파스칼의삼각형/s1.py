import sys
sys.stdin = open('input.txt')

T = int(input())
result = 0
for tc in range(1, T+1):
    n = int(input())
    arr = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(i+1):
            if j == 0 or j == n:
                arr.append(1)



    print(result)
