import itertools

n, m = map(int, input().split())
cards = list(map(int, input().split()))

flag_set = m
ans = 0
for card_set in itertools.permutations(cards, 3):
    temp = sum(card_set)
    flag = m - temp
    if 0 <= flag and flag < flag_set:
        flag_set = flag
        ans = temp
print(ans)