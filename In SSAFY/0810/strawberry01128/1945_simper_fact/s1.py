import sys

sys.stdin = open('input.txt')
T = int(input())
for test_case in range(1,T+1):
    insu_angry = int(input())
    a = 0
    b=0
    c=0
    d=0
    e=0

    while True:
        if insu_angry % 11 == 0:
            e += 1
            insu_angry = insu_angry / 11
        else:
            break

    while True:
        if insu_angry % 7 == 0:
            d += 1
            insu_angry = insu_angry / 7
        else:
            break

    while True:
        if insu_angry % 5 == 0:
            c += 1
            insu_angry = insu_angry / 5
        else:
            break

    while True:
        if insu_angry % 3 == 0:
            b += 1
            insu_angry = insu_angry / 3
        else:
            break
    while True:
        if insu_angry % 2 == 0:
            a += 1
            insu_angry = insu_angry / 2
        else:
            break

    print(f'#{test_case} {a} {b} {c} {d} {e}')
