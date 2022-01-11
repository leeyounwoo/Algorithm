import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T +1):
    N, hexadec = input().split()
    # 16 -> 10 -> 2

    # 16 -> 10
    # int()함수는 기본값으로 int(x, base=10)
    dec = int(hexadec, 16)
    # '47FE' -> 18430

    # 10 -> 2
    bi = format(dec, 'b')

    # 18430 -> '100011111111110'
    if len(bi) < int(N)*4 : # hex자리 수 = di * 4
        bi = '0'+bi

    print('#{} {}'.format(tc, bi))