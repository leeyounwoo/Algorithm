import sys
sys.stdin = open('input.txt')

TC = int(input())
for tc in range(1, TC+1):
    K,N,M = map(int,input().split())
    station = list(map(int, input().split()))
    station_lst = [0] * (N+1)

    for i in range(len(station)):
        station_lst[station[i]] += 1

    curr = 0
    temp = 0
    ans = 0
    flag = False

    while True:
        temp += K
        while True:
            if temp >= N:
                curr = temp
                break

            if station_lst[temp]:
                curr = temp
                ans += 1
                break
            else:
                temp -= 1

            if temp == curr:
                flag = True
                break
        if flag:
            ans = 0
            break
        if curr >= N:
            break

    print('#%s %d'%(tc, ans))