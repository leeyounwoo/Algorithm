for T in range(1, 1+int(input())):
    N = int(input())
    cards = list(map(str, input().split()))
    if N == 1:
        print('#{} {}'.format(T, cards[0]))
    else:
        first_cards = []
        second_cards = []
        middle, r = divmod(N, 2)
        if not r:
            middle -= 1
        for i in range(len(cards)):
            if i <= middle:
                first_cards.append(cards[i])
            else:
                second_cards.append(cards[i])

        print('#{}'.format(T), end=' ')
        while first_cards or second_cards:
            print(first_cards.pop(0), end=' ')
            if second_cards:
                print(second_cards.pop(0), end=' ')
        print()