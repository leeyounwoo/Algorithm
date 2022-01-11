import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cards = list(input().split())
    front_cards = cards[:(len(cards)+1)//2]
    back_cards = cards[(len(cards)+1)//2:]
    shuffle_cards = []

    while back_cards:
        shuffle_cards.append(front_cards.pop(0))
        shuffle_cards.append(back_cards.pop(0))

    if front_cards:
        shuffle_cards.append(front_cards.pop())

    print('#{}'.format(tc), *shuffle_cards)