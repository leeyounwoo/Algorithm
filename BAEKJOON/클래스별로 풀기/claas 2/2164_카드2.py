from collections import deque

n = int(input())
cards = deque([i for i in range(1, 1+n)])
while len(cards) >= 2:
    cards.popleft()
    cards.append(cards.popleft())
print(cards[0])