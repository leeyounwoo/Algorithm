import sys
sys.stdin = open('input.txt')

T = int(input())

def bruteforce(p, t) :
    i = 0
    j = 0
    M = len(p)
    N = len(t)
    while j < M and i < N:
        if t[i] != p[j]:
            i = i-j
            j = -1
        i = i+1
        j = j+1
    if j == M:
        return 1
    else:
        return 0

for tc in range(1, T+1):
    p = input()
    t = input()
    print('#{} {}'.format(tc, bruteforce(p, t)))