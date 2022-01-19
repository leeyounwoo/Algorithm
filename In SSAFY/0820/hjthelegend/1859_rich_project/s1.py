import sys

sys.stdin = open('input.txt')

# t = int(input())
#
# for tc in range(1, t+1):
#     n = int(input())
#     cost = list(map(int, input().split())) # 가격들을 입력을 받았다.
#     ans = 0
#
#     # 어디서 많이 본것 같다.
#     for i in range(n-1): # 어차피 마지막날은 사도그만 안사도 그만
#         max_cost = cost[i]
#         for j in range(i+1 ,n):
#             if max_cost < cost[j]:
#                 max_cost = cost[j]
#
#         if max_cost > cost[i]:
#             ans += max_cost - cost[i] # 이익을 구하자 !!
#
#     print("#{} {}".format(tc, ans))

# 팔 수 있는지 없는지 체크
# t = int(input())
#
# for tc in range(1, t+1):
#     n = int(input())
#     cost = list(map(int, input().split())) # 가격들을 입력을 받았다.
#     ans = 0
#
#     is_sell = [False] * n
#
#     # 사는게 이득인지 아닌지를 체크
#     for i in range(n-1):
#         for j in range(i+1, n):
#             if cost[i] < cost[j]:
#                 is_sell[i] = True
#                 break
#     buy_cost = 0
#     buy_cnt = 0
#
#     for i in range(n):
#         if is_sell[i]:
#             buy_cost += cost[i]
#             buy_cnt += 1
#         else:
#             ans += (cost[i]*buy_cnt) - buy_cost
#             buy_cost = 0
#             buy_cnt = 0
#
#     print('#{} {}'.format(tc, ans))
#
#########################
# 반대로 생각
t = int(input())

for tc in range(1, t+1):
    n = int(input())
    cost = list(map(int, input().split())) # 가격들을 입력을 받았다.
    ans = 0

    max_cost = cost[-1]

    for i in range(n-2, -1, -1):
        # 내가 가진 값보다 보고 있는 값이 작을때
        if max_cost > cost[i]:
            ans += max_cost - cost[i]

        else:
            max_cost = cost[i]

    print('#{} {}'.format(tc, ans))