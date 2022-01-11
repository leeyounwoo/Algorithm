import sys
sys.stdin = open('input.txt')

mlist = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

T = int(input())
for tc in range(1, T+1):
    money = int(input())
    check = [0] * 8

    for i in range(len(mlist)): #8-> 0~7
        while money - mlist[i] >= 0:
            money -= mlist[i]
            check[i] += 1

    print('#{}'.format(tc))
    print(*check)

