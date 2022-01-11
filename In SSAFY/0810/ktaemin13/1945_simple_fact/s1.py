import sys
sys.stdin = open('input.txt') # N=2**a x 3**b x 5**c x 7**d x 11**e

T = int(input())

for tc in range(T):
    numbers = int(input())

    factor_list = []
    factorization = [2, 3, 5, 7, 11]
    for div in factorization:
        cnt = 0
        while numbers % div == 0:
            numbers = numbers // div
            cnt += 1

        factor_list.append(cnt)

    print('#{0}'.format(tc+1), *factor_list)