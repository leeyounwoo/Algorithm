import sys
sys.stdin = open('0929/woosteelz/1260_단순2진코드/input.txt')

secret_code = {
    '0001101': 0,
    '0011001': 1,
    '0010011': 2,
    '0111101': 3,
    '0100011': 4,
    '0110001': 5,
    '0101111': 6,
    '0111011': 7,
    '0110111': 8,
    '0001011': 9
}


def change_code(code):
    temp = ''
    res = []
    for i in range(56):
        temp += code[i]
        if len(temp) % 7 == 0:
            res.append(secret_code[temp])
            temp = ''
    return res


for tc in range(int(input())):
    n, m = map(int, input().split())

    secret = [input() for _ in range(n)]

    for i in range(n):
        if '1' in secret[i]:
            temp = secret[i]
            break

    code = ''
    for token in temp[::-1]:
        if len(code) == 56:
            break
        if token == '1':
            code = token + code
        elif code:
            code = token + code

    code = change_code(code)
    ans = 0
    for i in range(len(code)):
        if not i % 2:
            ans += code[i] * 3
        else:
            ans += code[i]
    res = 0
    if not ans % 10:
        res = sum(code)

    print(f'#{tc+1} {res}')
