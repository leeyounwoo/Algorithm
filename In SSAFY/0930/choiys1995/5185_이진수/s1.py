import sys
sys.stdin = open('input.txt')

T = int(input())

# 10 이 넘는 숫자를 위한 변환기
converter = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

for tc in range(1, T+1):
    N, number = input().split()
    result = ''
    # 읽는거는 뒤부터
    for n in number[::-1]:
        # 변환기 안에 있는 숫자 변환
        if n in converter:
            n = converter[n]
        # 변환기 안에 없는 숫자는 바로 int
        n = int(n)
        # 16진수는 한자리당 최대 bin(1111)까지 차지하는 수
        # 무조건 4자리 차지하니 2진번 변환을 4번 반복해준다.
        for _ in range(4):
            result = str(n % 2) + result
            n //= 2

    print("#{} {}".format(tc, result))