import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    result = []
    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    for i in money:
        if N >= i:
            result.append(N//i)
            N = N % i
        else:
            result.append(0)
    print('#{}'.format(tc))
    print(' '.join(map(str, result)))

