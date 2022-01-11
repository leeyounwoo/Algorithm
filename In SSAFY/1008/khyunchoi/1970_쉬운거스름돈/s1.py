import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    coin_list = []
    a = 50000

    for _ in range(4):
        coin_list.append(N//a)
        N %= a
        a //= 5
        coin_list.append(N//a)
        N %= a
        a //= 2

    result = ' '.join(map(str, coin_list))
    print('#{}'.format(tc))
    print(result)