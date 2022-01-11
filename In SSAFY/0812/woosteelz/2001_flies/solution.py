import sys
sys.stdin = open('input.txt')

TC = int(input())
for tc in range(TC):
    n, m = map(int, input().split())
    flies = [list(map(int, input().split())) for _ in range(n)]
    # ans = float('-inf')
    ans = -100

    for i in range(n - m + 1):
        for j in range(n - m + 1):
            temp = 0
            for x in range(i, i + m):
                for y in range(j, j + m):
                    temp += flies[x][y]
            if temp > ans:
                ans = temp

    print('#{} {}'.format(tc+1, ans))