import sys
sys.stdin = open('input.txt')


def paper(n):
    idx = n//10 - 1
    f = [1, 3]
    for i in range(2, idx+1):
        f.append(2 * f[i-2] + f[i-1])

    return f[idx]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    print('#{} {}'.format(tc, paper(N)))