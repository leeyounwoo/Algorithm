import sys

sys.stdin = open('input.txt')

# 1. 모든 노선 체크
# def bus_count(bus_stop):
#     cnt = 0
#
#     for i in range(n):
#         if bus_route[i][0] <= bus_stop <= bus_route[i][1]:
#             cnt += 1
#
#     return cnt
#
#
# t = int(input())
# for tc in range(1, t+1):
#     n = int(input()) # 버스 노선 수
#
#     bus_route = [] # 버스의 노선들을 저장해 놓을 리스트
#
#     for i in range(n):
#         a, b = map(int, input().split())
#         bus_route.append((a, b))
#
#     # 내가 확인하고 싶은 정류장의 개수
#     p = int(input())
#     ans = [] # 버스 수를 저장해 놓을 리스트
#
#     for i in range(p):
#         c = int(input())
#         ans.append(bus_count(c))
#
#     print('#{}'.format(tc), end=' ')
#     print(' '.join(map(str, ans)))

############################################ 정류장 미리계산
#
# t = int(input())
# for tc in range(1, t+1):
#     n = int(input()) # 버스 노선 수
#
#     start = [0] * 5001 # 출발 정류장 표시
#     end = [0] * 5001 #도착 정류장 표시
#     bus_stop = [0] * 5001 # 계산한 버스 표시
#
#     for i in range(n):
#         a, b = map(int, input().split())
#         start[a] += 1
#         end[b] += 1
#
#     for i in range(len(bus_stop)-1):
#         bus_stop[i+1] = bus_stop[i] - end[i] + start[i+1]
#
#     p = int(input())
#     print("#{}".format(tc), end=" ")
#     for i in range(p):
#         c = int(input()) # 우리가 확인하고 싶은 정류장 번호
#         print(bus_stop[c], end=' ')
#     print()
###################################################################################### 미리계산 2
t = int(input())
for tc in range(1, t+1):
    n = int(input()) # 버스 노선 수

    bus_stop = [0] * 5001

    for i in range(n):
        a, b = map(int, input().split())

        for j in range(a, b+1):
            bus_stop[j] += 1

    p = int(input())
    print('#{}'.format(tc), end=' ')
    for i in range(p):
        c = int(input()) # 우리가 확인하고 싶은 정류장 번호.
        print(bus_stop[c], end=' ')
    print()