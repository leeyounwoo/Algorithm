import sys
sys.stdin = open('input.txt')
password = {
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


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    num = [input() for _ in range(N)]
    result = []
    total = 0
    ans = 0
    for i in range(N):
        for j in range(M-1, -1, -1):
            if num[i][j] == '1':
                data = num[i][j-55:j+1]
                break
    for k in range(0, len(data), 7):
        temp = ''
        for l in range(k, k+7):
            temp += data[l]
        result.append(password[temp])
    for m in range(1, 8):
        if m % 2:
            total += 3 * result[m-1]
        else:
            total += result[m-1]
    total += result[7]
    if total % 10 == 0:
        for n in range(len(result)):
            ans += result[n]
    else:
        ans = 0
    print('#{} {}'.format(tc, ans))
