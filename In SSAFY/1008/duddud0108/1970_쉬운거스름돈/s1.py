import sys
sys.stdin = open('input.txt')

T = int(input())
change = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
for tc in range(1, T + 1):
    money = int(input())
    change_num = []
    for m in change:
        change_num.append(money // m)
        money = money % m
    print('#{}'.format(tc))
    print(*change_num)

