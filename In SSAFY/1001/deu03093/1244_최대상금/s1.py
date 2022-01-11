import sys
sys.stdin = open('input.txt')
from collections import deque

for T in range(1, 1+int(input())):
    number, cnt = map(int, input().split())
    cards = [int(i) for i in str(number)]
    card_list = deque()
    card_list.append(cards)
    for count in range(cnt):
        length_card = len(card_list)
        flag_cnt = False
        # print(length_card)
        # 이전 card_list에 있는 것들 순회
        for c in range(length_card):
            cards = card_list.popleft()
            # print(count, c, cards)
            for i in range(len(cards)-1):
                left_index = i
                left_value = cards[i]
                temp = cards[left_index+1:]
                right_value = max(temp)
                if left_value < right_value:
                    max_list = []
                    for j in range(len(cards)):
                        if cards[j] == right_value:
                            max_list.append(j)
                    for max_index in max_list:
                        cards[left_index], cards[max_index] = cards[max_index], cards[left_index]
                        card_list.append(cards[:])
                        cards[left_index], cards[max_index] = cards[max_index], cards[left_index]
                        flag_cnt = True
                    # print(card_list)

                    break
                else:
                    if left_index == len(cards)-2:
                        dict_cards = {}
                        # print(dict_cards)
                        # print((cards[1]))
                        for d in range(len(cards)):
                            if cards[d] in dict_cards:
                                dict_cards[cards[d]] += 1

                            else:
                                dict_cards[cards[d]] = 1
                                # print(dict_cards)
                        # print(dict_cards)
                        for key, value in dict_cards.items():
                            if value >= 2:
                                card_list.append(cards[:])
                        else:
                            cards[left_index], cards[left_index+1] = cards[left_index+1], cards[left_index]
                            card_list.append(cards[:])
                            cards[left_index], cards[left_index+1] = cards[left_index+1], cards[left_index]
                    # print(left_value, right_value)
                    # print('continue')
                    continue

    answers = []
    for cards in card_list:
        ans = 0
        for i in range(len(cards)-1, -1, -1):
            ans += cards[len(cards)-1-i] * (10**i)
        answers.append(ans)
    # print(answers)
    print('#{} {}'.format(T, max(answers)))