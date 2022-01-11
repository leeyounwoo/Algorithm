import sys

sys.stdin = open('input.txt')

T = int(input())

for _ in range(T):
    number = int(input())
    numbers = []
    for i in range(6):
        numbers.append(number % 10)
        number = number // 10

    cards = [0] * 10
    for i in range(len(numbers)):
        cards[numbers[i]] += 1

    triplet = 0
    i = 0
    for i in range(len(cards)):
        if cards[i] == 6:
            triplet += 2
            cards[i] -= 6
        elif cards[i] >= 3:
            triplet += 1
            cards[i] -= 3

    run = 0
    i = 0
    for i in range(len(cards)-2):
        if cards[i] == 2 and cards[i+1] == 2 and cards[i+2] == 2:
            run += 2
            cards[i] -= 2
            cards[i+1] -= 2
            cards[i+2] -= 2
        elif cards[i] == 1 and cards[i+1] == 1 and cards[i+2] == 1:
            run += 1
            cards[i] -= 1
            cards[i + 1] -= 1
            cards[i + 2] -= 1

    if triplet + run == 2:
        print('baby-gin')
    else:
        print('fail')