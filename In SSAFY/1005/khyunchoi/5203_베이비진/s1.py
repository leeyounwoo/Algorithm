import sys
sys.stdin = open('input.txt')


def judge_run(arr):
    for i in range(len(arr)):
        if arr.count(arr[i] + 1) and arr.count(arr[i] + 2):
            return True


def judge_triplet(arr):
    for i in range(10):
        if arr.count(i) == 3:
            return True


T = int(input())
for tc in range(1, T+1):
    cards = list(map(int, input().split()))
    A_cards, B_cards = [], []
    for i in range(len(cards)):
        if i % 2:
            B_cards.append(cards[i])
        else:
            A_cards.append(cards[i])

    A_result = 6
    for i in range(2, len(A_cards)):
        if judge_run(A_cards[:i + 1]) or judge_triplet(A_cards[:i + 1]):
            A_result = i
            break
    B_result = 6
    for i in range(2, len(B_cards)):
        if judge_run(B_cards[:i + 1]) or judge_triplet(B_cards[:i + 1]):
            B_result = i
            break

    result = 0
    if A_result != 6 and A_result <= B_result:
        result = 1
    elif A_result > B_result:
        result = 2

    print('#{} {}'.format(tc, result))