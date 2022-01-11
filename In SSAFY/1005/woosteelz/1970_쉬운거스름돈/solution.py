import sys
sys.stdin = open('1005/woosteelz/1970_쉬운거스름돈/input.txt')

change = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
for tc in range(int(input())):
    ans = []
    money = int(input())
    for cost in change:
        ans.append(str(money // cost))
        money = money % cost
    print(f'#{tc + 1}\n{" ".join(ans)}')
