import sys

sys.stdin = open('input.txt')
# 연속된 N일 동안 물건의 매매가 예측
# 하루에 최대 1만큼 구입
# 판매는 얼마든지
# 최대 이익을 출력해라

# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     cost = list(map(int, input().split()))  # 가격들을 입력을 받았다.
#
#     ans = 0
#
#     for i in range(N-1) : #왜 N-1? 어차피 마지막 날은 사도 그만~안 사도 그만~
#         max_cost = cost[i]
#         for j in range(i+1, N):
#             if max_cost < cost[j] :
#                 max_cost = cost[j]
#         if max_cost > cost[i] :
#             ans += max_cost - cost[i] # 이익을 구하자!!!
#     print('{} {}'.format(tc, ans))
###################################
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     cost = list(map(int, input().split()))  # 가격들을 입력을 받았다.
#
#     ans = 0
#
#     is_sell = [False] * N  # 사서 팔지 말지
#     # 사는게 이득인지 아닌지를 check
#     for i in range(N - 1):
#         for j in range(i + 1, N):
#             if cost[i] < cost[j]:
#                 is_sell[i] = True
#                 break
#
#     buy_cost = 0
#     buy_cnt = 0
#     for i in range(N):
#         if is_sell[i]:
#             buy_cost += cost[i]
#             buy_cnt += 1
#         else:
#             ans += (cost[i] * buy_cnt) - buy_cost
#             buy_cost = 0
#             buy_cnt = 0
#     print('#{} {}'.format(tc, ans))
##################
# 반대로 생각각
T= int(input())
for tc in range(1, T + 1):
    N = int(input())
    cost = list(map(int, input().split()))  # 가격들을 입력을 받았다.

    ans = 0
    max_cost = cost[-1] #마지막 값
    for i in range(N-2, -1,-1):  # 왜 -2? -1 (어차피 마지막에 있는 애는 필요 없음!)
        # 내가 가진 값보다 보고 잇는 값이 작을 때
        if max_cost > cost[i] :
            ans += max_cost - cost[i]
        else :
            max_cost = cost[i]
    print('#{} {}'.format(tc, ans))