import sys
sys.stdin = open('input.txt')

for l in range(1, 11):
    r = int(input())
    b = list(map(int, input().split()))
    c = 0

    for i in range(2, r-2):

        m = max(b[i+1], b[i+2], b[i-1], b[i-2])

        if b[i] - m > 0:
            c += b[i] - m
    print("#{} {}".format(l, c))
