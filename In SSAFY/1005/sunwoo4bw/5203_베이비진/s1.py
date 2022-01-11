import sys
sys.stdin = open('input.txt')
# 연속인 숫자가 3개 이상이면 run
# 같은 숫자가 3개 이상이면 triplet
# 두 사람이 번갈아 가며
T = int(input())
for tc in range(1, T+1):
    cards = list(map(int,input().split()))
    # [9 9 5 6 5 6 1 1 4 2 2 1]

    first = [0] * 10 # 카드 체크
    second = [0] * 10 # 카드 체크

    winner = 0
    for c in range(0, 12, 2): # 6장의 카드를 두명이 번갈아
        first[cards[c]] += 1   # 0 2 4 6 8 10
        second[cards[c+1]] += 1 # 1 3 5 7 9 11
        samenum_f = max(first)  # 0또는 1이 아닌 숫자 -> 반복
        samenum_s = max(second)

        for i in range(1, 9): # triplet이거나 run인지 확인
            if first[i-1] >= 1 and first[i] >= 1 and first[i+1] >= 1 or samenum_f >= 3  :
                winner = 1
        if winner != 0:
            break
        for i in range(1, 9):
            if second[i-1] >= 1 and second[i] >= 1 and second[i+1] >= 1 or samenum_s >= 3 :
                winner = 2
        if winner != 0:
            break
    print('#{} {}'.format(tc, winner))