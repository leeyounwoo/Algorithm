import sys
sys.stdin = open('input.txt')


T = int(input())

answer = []
for tc in range(1, T + 1):

    day_price, month_price, trimonth_price, year_price = map(int, input().split())
    year_plan = list(map(int, input().split()))

    dp = [0] * (len(year_plan) + 1)

    for i in range(1, len(year_plan)+1):
        if i >= 12:
            dp[i] = min((dp[i-1] + (day_price * year_plan[i-1])), (dp[i-1] + month_price), (dp[i-3] + trimonth_price), (dp[i-12] + year_price))
        elif i >= 3:
            dp[i] = min((dp[i-1] + (day_price * year_plan[i-1])), (dp[i-1] + month_price), (dp[i-3] + trimonth_price))
        else:
            dp[i] = min((dp[i-1] + (day_price * year_plan[i-1])), (dp[i-1] + month_price))

    result = dp[len(year_plan)]
    answer.append(result)

for tc in range(1, T + 1):
    print(f'#{tc} {answer[tc-1]}')