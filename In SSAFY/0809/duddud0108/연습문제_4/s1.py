import sys
sys.stdin = open('input.txt')

T = int(input())

for _ in range(T):
    card = input()
    counts = [0]*10
    run = 0
    triplet = 0

    for i in range(6):
        counts[int(card[i])] += 1

    i = 0
    while i < 10:
        if counts[i] >= 3:
            triplet += 1
            counts[i] -= 3
            continue

        if counts[i] and counts[i+1] and counts[i+2]:
            run += 1
            counts[i] -= 1
            counts[i+1] -= 1
            counts[i+2] -= 1
            continue

        if not counts:
            break

        i += 1

    print(run+triplet == 2)
