import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(T):

    cards = list(map(int, input()))

    digits = [0] * 10
    for card in cards:
        digits[card] += 1

    run = 0
    triplet = 0
    i = 0
    result = 'No'
    while i < 10:
        if digits[i] >= 3:
            triplet += 1
            digits[i] -= 3
            continue
        elif i < 8 and (digits[i] > 0 and digits[i+1] > 0 and digits[i+2] > 0):
            run += 1
            digits[i] -= 1
            digits[i+1] -= 1
            digits[i+2] -= 1
            continue
        if run + triplet == 2:
            result = 'baby-gin'
            break
        i += 1

    print(result)



