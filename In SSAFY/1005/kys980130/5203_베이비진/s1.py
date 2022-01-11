import sys
sys.stdin = open('input.txt')
def babygin(cards):
    cards.sort()
    for j in range(len(cards)-2):
        if cards[j]+1 == cards[j+1] and cards[j+1]+1 == cards[j+2]:
            return 1
        elif cards[j-1]+1 == cards[j] and cards[j]+1 == cards[j+1]:
            return 1
        elif cards[j-2]+1 == cards[j-1] and cards[j-1]+1 == cards[j]:
            return 1
        elif cards[j] == cards[j+1] == cards[j+2]:
            return 1
        elif cards[j-1] == cards[j] == cards[j+1]:
            return 1
        elif cards[j-2] == cards[j-1] == cards[j]:
            return 1

T = int(input())
for tc in range(1, T+1):
    numbers = list(map(int, input().split()))
    player1 = [numbers[0], numbers[2]]
    player2 = [numbers[1], numbers[3]]
    result = 0
    for i in range(5, 13):
        if i % 2:
            player1.append(numbers[i-1])
            if babygin(player1) == 1:
                result = 1
                break
        else:
            player2.append(numbers[i-1])
            if babygin(player2) == 1:
                result = 2
                break
    print('#{} {}'.format(tc, result))

