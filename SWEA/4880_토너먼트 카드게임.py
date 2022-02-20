def tournament(cards, start, end):
    if start == end:
        return start

    middle = (start + end) // 2
    left_idx = tournament(cards, start, middle)
    right_idx = tournament(cards, middle + 1, end)

    win_idx = left_idx
    flag = cards[left_idx] - cards[right_idx]
    if flag == -1 or flag == 2:
        win_idx = right_idx

    return win_idx


for T in range(1, 1 + int(input())):
    N = int(input())
    cards = list(map(int, input().split()))
    ans = tournament(cards, 0, N - 1)
    print('#{} {}'.format(T, ans + 1))