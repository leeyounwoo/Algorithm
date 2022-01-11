import sys

sys.stdin = open('input.txt')

T = int(input())

for t in range(T) :
    numbers = input()
    count = [0]*10
    run = triplet = 0

    for number in numbers :
        count[int(number)] += 1

    i =0
    while i < 10 :
        if count[i] and count[i+1] and count[i+2] :
            run += 1
            count[i] -= 1
            count[i+1] -= 1
            count[i+2] -= 1
            continue
        elif count[i] >= 3 :
            triplet += 1
            count[i] -= 3
            continue
        i += 1

    if run + triplet == 2 :
        print('Baby-gin')
    else :
        print('No')