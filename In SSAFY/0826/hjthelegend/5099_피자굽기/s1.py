import sys
sys.stdin = open('input.txt')
from collections import deque

t = int(input())
for tc in range(1, t+1):
    n, pizza = map(int, input().split())
    cheese = list(map(int, input().split()))
    # 한 바퀴 -> 치즈의 양은 반으로
    # C // 2
    # 치즈는 순서대로 넣는다.
    idx = [i+1 for i in range(pizza)] # 총 피자 개수의 인덱스
    idx1 = deque(idx[:n]) # 오븐을 위한 idx
    idx2 = deque(idx[n:]) # 남겨진 피자를 위한 idx
    oven = deque(cheese[:n])
    left = deque(cheese[n:])

    answer = 0

    while len(oven) > 1:
        popped = oven.popleft()
        popped = popped // 2
        popped_idx = idx1.popleft()
        if popped == 0:
            if left:
                oven.append(left.popleft())
                idx1.append(idx2.popleft())
        elif popped > 0:
            oven.append(popped)
            idx1.append(popped_idx)

    answer = idx1[0]
    print('#{} {}'.format(tc, answer))
    # print(oven, 'oven')
    # print(left)
    # print(idx1)
    # print(idx2)
    # print(answer)