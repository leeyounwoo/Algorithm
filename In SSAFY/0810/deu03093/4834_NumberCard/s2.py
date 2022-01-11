import sys

sys.stdin = open('input.txt')

for T in range(1, int(input()) + 1):
    n = int(input())
    # 08271
    cards = input()
    # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] : 0 ~ 9
    counts = [0] * 10

    # [1, 1, 1, 0, 0, 0, 0, 1, 1, 0]
    for i in range(len(cards)):
        counts[int(cards[i])] += 1

    # max_count = 1
    max_count = counts[0]
    for i in range(len(counts)):
        if max_count < counts[i]:
            max_count = counts[i]

    # 카드 장수가 같을 때는 적힌 숫자가 큰 쪽을 출력
    for i in range(len(counts) - 1, -1, -1):
        if counts[i] == max_count:
            max_num = i
            break

    print('#{} {} {}'.format(T, max_num, max_count))
