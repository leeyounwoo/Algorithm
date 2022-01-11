import sys

def paper(n):
    d = [1, 3]
    for i in range(2, n):
        d.append(d[i-1] + 2 * d[i-2])
    return d[n-1]


sys.stdin = open('input.txt')
for T in range(1, 1 + int(input())):
    n = int(input())
    ans = paper(n//10)
    print('#{} {}'.format(T, ans))