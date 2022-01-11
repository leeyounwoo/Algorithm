import sys

sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T+1) :
    N = int(input())
    numbers = input()
    check = [0]*10

    for n in numbers :
        check[int(n)] += 1

    max_ch = check[0]
    for ch in check :
        if ch > max_ch :
            max_ch = ch

    for i in range(len(check)-1, -1, -1) :
        if check[i] == max_ch :
            print(f'#{t} {i} {max_ch}')
            break