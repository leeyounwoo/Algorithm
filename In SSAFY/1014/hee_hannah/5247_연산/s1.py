import sys
sys.stdin = open('input.txt')

def find(n,m):
    cnt = 0
    check = []
    check.append(n)
    if n == m:
        li.apppend(cnt)

    else:
        if 0 <= n <= 1000000 and n not in check:
            cnt += 1
            find(n - 1, m)
            find(n + 1, m)
            find(n*2, m)
            find(n-10, m)



t = int(input())
for tc in range(1, t+1):
    print('#{}'.format(tc), end=" ")
    n, m = map(int, input().split())
    li = []
    find(n, m)
    print(min(li))