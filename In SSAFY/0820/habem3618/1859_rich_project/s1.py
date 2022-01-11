import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cost_lst = list(map(int, input().split()))

    ans = 0
    max_cost = cost_lst[-1]

    for i in range(N-2, -1, -1):
        if max_cost > cost_lst[i]:
            ans += max_cost - cost_lst[i]
        else:
            max_cost = cost_lst[i]
    print("#{} {}".format(tc, ans))
