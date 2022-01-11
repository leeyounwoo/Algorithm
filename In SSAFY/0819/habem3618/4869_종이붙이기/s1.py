import sys
sys.stdin = open("input.txt")

def cut_paper(n):
    f = [1, 1]

    for i in range(2, n+1):
        f.append(f[i-1] + 2*f[i-2])

    return f[n]

T = int(input())
for tc in range(T):
    N = int(input())//10
    print('#{} {}'.format(tc+1, cut_paper(N)))