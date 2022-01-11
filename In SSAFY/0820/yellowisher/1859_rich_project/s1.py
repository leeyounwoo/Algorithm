import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(T):
    N = int(input())
    cost = list(map(int, input().split()))

    ans = 0

    max_cost = cost[-1]
    for i in range(N - 2, -1, -1):
        # 내가 가진 값보다 보고 있는 값이 작을 때

        if max_cost > cost[i]:
            ans += max_cost - cost[i]
        else:
            max_cost = cost[i]

    print("#{} {}".format(tc, ans))
