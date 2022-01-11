import sys
sys.stdin = open('input.txt')

def match(i, j):
    if card[i] == 1 and (card[j] == 1 or card[j] == 3):
        return i
    elif card[i] == 2 and (card[j] == 2 or card[j] == 1):
        return i
    elif card[i] == 3 and (card[j] == 3 or card[j] == 2):
        return i
    return j


def winner(i, j):
    if i == j:
        return i

    first = winner(i, (i+j)//2)
    second = winner((i+j)//2+1, j)

    return match(first, second)


for tc in range(int(input())):
    num = int(input())
    card = list(map(int, input().split()))

    print('#{} {}'.format(tc+1, winner(0, num-1) + 1))
