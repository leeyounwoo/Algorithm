import sys

sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T+1) :
    N = int(input())

    fact = [2, 3, 5, 7, 11]
    result = [0]*5

    while N > 1 :
        for i in range(len(fact)) :
            if not N%fact[i] :
                result[i] += 1
                N /= fact[i]

    print(f'#{t}', end = ' ')

    for j in range(len(fact)) :
        if fact[j] == 11 :
            print(f'{result[j]}')
        else :
            print(f'{result[j]}', end = ' ')