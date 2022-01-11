import sys
sys.stdin = open('input.txt')

n = {'0001101':0,'0011001':1,'0010011':2,'0111101':3,'0100011':4,
    '0110001':5,'0101111':6, '0111011':7,'0110111':8,'0001011':9}

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    code = [input() for _ in range(N)]
    found = False
    for i in range(N):
        for j in range(M-1, -1, -1):
            # 모든 암호코드는 1로 끝난다.
            # 1을 뒤에서 찾으면 거기서부터 잘라서 암호코드 확인
            if code[i][j] == '1':
                r_idx = i
                c_idx = j
                found = True
                break
        if found:
            break
    # 암호코드 마지막 idx - 첫 idx == 55
    t = code[r_idx][c_idx-55:c_idx+1]
    even, odd = 0, 0
    # 7자리씩 끊어서 even과 odd에 저장
    for k in range(7):
        if k % 2 == 0:
            even += n[t[7*k:7*(k+1)]]
        else:
            odd += n[t[7*k:7*(k+1)]]
    r = even * 3 + odd
    # t[-7:] == 마지막 7자리 수 / n[t[-7:]] == 검증코드
    if (r+n[t[-7:]]) % 10 != 0:
        r = 0
    else:
        r = even + odd + n[t[-7:]]
    print("#{} {}".format(tc, r))