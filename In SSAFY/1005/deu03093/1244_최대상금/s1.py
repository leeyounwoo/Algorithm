import sys
sys.stdin = open('input.txt')
from collections import deque
32888


for T in range(1, 1+int(input())):
    number, cnt = map(int, input().split())
    cards = [int(i) for i in str(number)]
    card_list = deque()
    card_list.append(cards)
    # 교환횟수만큼 반복
    for count in range(cnt):
        length_card = len(card_list)
        # 경우의 수만큼 반복
        for c in range(length_card):
            cards = card_list.popleft()
            # 바꿀 왼쪽 위치 선택
            for i in range(len(cards)-1):
                left_index = i
                left_value = cards[i]
                temp = cards[left_index+1:]
                right_value = max(temp)
                # 왼쪽 위치 선택!
                if left_value < right_value:
                    max_list = []
                    for j in range(len(cards)):
                        if cards[j] == right_value:
                            max_list.append(j)
                    for max_index in max_list:
                        cards[left_index], cards[max_index] = cards[max_index], cards[left_index]
                        card_list.append(cards[:])
                        cards[left_index], cards[max_index] = cards[max_index], cards[left_index]
                    break
                # 없는 경우
                else:
                    # 만약 끝에서 2번째인 경우(현재 정렬되어 있는 상태)
                    if left_index == len(cards)-2:
                        dict_cards = {}
                        for d in range(len(cards)):
                            if cards[d] in dict_cards:
                                dict_cards[cards[d]] += 1
                            else:
                                dict_cards[cards[d]] = 1
                        # 같은 값이 있으면 그거끼리 바꿔줌
                        for key, value in dict_cards.items():
                            if value >= 2:
                                card_list.append(cards[:])
                        # 같은 값이 없으면 끝값끼리 바꿔줌
                        else:
                            cards[left_index], cards[left_index+1] = cards[left_index+1], cards[left_index]
                            card_list.append(cards[:])
                            cards[left_index], cards[left_index+1] = cards[left_index+1], cards[left_index]
                    continue

    answers = []
    for cards in card_list:
        ans = 0
        for i in range(len(cards)-1, -1, -1):
            ans += cards[len(cards)-1-i] * (10**i)
        answers.append(ans)
    print('#{} {}'.format(T, max(answers)))