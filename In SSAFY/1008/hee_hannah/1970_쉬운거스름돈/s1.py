import sys
sys.stdin = open('input.txt')

li = [50000,10000,5000,1000,500,100,50,10]

T = int(input())
for tc in range(1,T+1):
    cnt = [0,0,0,0,0,0,0,0]
    money = int(input())
    for i in range(1, len(li)+1):
        if (money // li[i-1]) >= 1: #몫 즉 돈보다 거스름돈이 작다면. 거슬러줄수잇다면
            cnt[i-1] = int(money // li[i-1])
            money = money % li[i-1]
        elif (money // li[i-1]) < 1:
            continue
    print('#{}'.format(tc))
    print(*cnt)