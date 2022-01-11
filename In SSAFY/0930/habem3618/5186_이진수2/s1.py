import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = float(input())
    result = [101]


    for i in range(1, 13):
        N *= 2
        result.append(int(N) % 2)
        if N % 1 == 0:
            break

    else:
        result = 'overflow'

    print("#{} {}".format(tc, ''.join(map(str, result))))
