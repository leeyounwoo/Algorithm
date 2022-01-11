# # 우철님 풀이
# import sys
# sys.stdin = open('input.txt')
#
# def match(i, j):
#     if card[i] == 1 and (card[j] == 1 or card[j] == 3):
#         return i
#     elif card[i] == 2 and (card[j] == 2 or card[j] == 1):
#         return i
#     elif card[i] == 3 and (card[j] == 3 or card[j] == 2):
#         return i
#     return j
#
#
# def winner(i, j):
#     if i == j:
#         return i
#
#     first = winner(i, (i+j)//2)
#     second = winner((i+j)//2+1, j)
#
#     return match(first, second)
#
#
# for tc in range(int(input())):
#     num = int(input())
#     card = list(map(int, input().split()))
#
#     print('#{} {}'.format(tc+1, winner(0, num-1) + 1))


#영하님 풀이
import sys
sys.stdin = open('input.txt')

def rsp(a, b):
    RSP = {1: (3, 2), 2: (1, 3), 3: (2, 1)}

    if numbers[a] == numbers[b]:
        return a
    elif RSP[numbers[a]][0] == numbers[b]:
        return a
    elif RSP[numbers[a]][1] == numbers[b]:
        return b

def tournament(start, end):
    if start == end:
        return start

    left = tournament(start, (start + end)//2)
    right = tournament((start + end)//2 + 1, end)

    return rsp(left, right)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    print('#{} {}'.format(tc, tournament(0, N-1)+1))