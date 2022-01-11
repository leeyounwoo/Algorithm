import sys
sys.stdin = open('input.txt')
def babygin(cards):
    for j in range(10):
        if j < 8 and cards[j] >= 1 and cards[j+1] >= 1 and cards[j+2] >= 1:
            return 1
        elif j < 9 and cards[j-1] >= 1 and cards[j] >= 1 and cards[j+1] >= 1:
            return 1
        elif cards[j-2] >= 1 and cards[j-1] >= 1 and cards[j] >= 1:
            return 1
        elif cards[j] >= 3:
            return 1


T = int(input())
for tc in range(1, T+1):
    numbers = list(map(int, input().split()))
    player1 = [0 for _ in range(10)]
    player2 = [0 for _ in range(10)]
    result = 0
    for i in range(1, 13):
        if i % 2:
            player1[numbers[i-1]] += 1
            if i >= 5:
                if babygin(player1) == 1:
                    result = 1
                    break
        else:
            player2[numbers[i-1]] += 1
            if i >= 6:
                if babygin(player2) == 1:
                    result = 2
                    break
    print('#{} {}'.format(tc, result))
