import sys
sys.stdin = open('input.txt')

numbers = {
    '0001101': '0',
    '0011001': '1',
    '0010011': '2',
    '0111101': '3',
    '0100011': '4',
    '0110001': '5',
    '0101111': '6',
    '0111011': '7',
    '0110111': '8',
    '0001011': '9'
}
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # N X M
    code = [input() for _ in range(N)]

    # 암호코드 뽑기
    # 처음으로 0으로 채워지지 않은 줄
    # c는 code의 1행
    for c in code:
        if not c == '0' * M:
            target = c
            break
            # target = 0000011101101100010111011011000101100010001101001001101110110000000000
            # = password를 포함한 행

    # 역순으로 처음으로 0이 아닌 곳
    for i in range(M - 1, 0, -1):
        if target[i] == '1':
            idx = i #
            break
            # idx = 59

    password = ''
    pwd = target[idx - 55:idx + 1]  # 앞/뒤 무의미한 0 빼고 슬라이싱 # 왜 55? # 암호코드의 가로는 56칸
    # pwd = 01110110110001011101101100010110001000110100100110111011

    # pwd = 0111011/0110001/0111011/0110001/0110001/0001101/0010011/0111011
    for i in range(0, 56, 7):
        password += numbers.get(pwd[i:i + 7])
        # 7/5/7/5/5/0/2/7

    # 검증코드 유효한지 확인
    # password = 75755027
    tmp = 0
    for index, p in enumerate(password): # 인덱스로 돌릴 거야
        if index % 2  == 1:
            tmp += int(p)
        else:
            tmp += int(p) * 3
    # tmp = 80
    if tmp % 10 == 0: # ok
        p_list = list(map(int, password))
        p_sum = sum(p_list)
    else:
        p_sum = 0

    print('#{} {}'.format(tc, p_sum))