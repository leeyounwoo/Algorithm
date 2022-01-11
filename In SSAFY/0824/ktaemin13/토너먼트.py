def play(cards, left, right):
    if left == right:
        return left, cards[left:right + 1][0]

    mid = (left + right) // 2
    p1_idx, p1_val = play(cards, left, mid) # 왼쪽 부분 재귀
    p2_idx, p2_val = play(cards, mid + 1, right) # 오른쪽 부분 재귀

    battle = {
        (1, 1): (p1_idx, p1_val),
        (1, 2): (p2_idx, p2_val),
        (1, 3): (p1_idx, p1_val),
        (2, 1): (p1_idx, p1_val),
        (2, 2): (p1_idx, p1_val),
        (2, 3): (p2_idx, p2_val),
        (3, 1): (p2_idx, p2_val),
        (3, 2): (p1_idx, p1_val),
        (3, 3): (p1_idx, p1_val),
    }
    return battle[(p1_val, p2_val)]  # 승자 반환


T = int(input())
for tc in range(1, 1 + T):
    N = int(input())
    cards = list(map(int, input().split()))

    result = play(cards, 0, len(cards) - 1)
    print('#{} {}'.format(tc, result[0] + 1))
