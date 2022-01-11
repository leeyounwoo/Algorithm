import sys
sys.stdin = open('input.txt')

for T in range(1, int(input()) + 1):
    money = int(input())
    result = [0] * 8
    ret_money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    for i in range(len(ret_money)):
        count, money = divmod(money, ret_money[i])
        result[i] = count
    print(f'#{T}')
    for i in result:
        print(i, end=' ')
    print()