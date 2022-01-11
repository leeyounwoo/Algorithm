import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = float(input())
    cnt = 0
    result = ''
    # 2진법 자리수 시작
    a = 1
    # N이 0이 될때까지
    while N:
        # 만약 N보다 2진법 자리가 크다면 0을 붙인다.
        if N < 2 ** -a:
            result += '0'
        # 아니라면 N에서 해당 값을 빼고 1을 붙인다.
        else:
            N -= 2 ** -a
            result += '1'
        # 붙이고 나서 횟수를 더해준다.
        cnt += 1
        # 만약 12회가 넘어간다면 overflow로 끝낸다.
        if cnt > 12:
            result = 'overflow'
            break
        # 아니라면 다음 자리수를 봐보자
        else:
            a += 1
    # 12자리까지 딱 나누어 떨어졌으면 결과값을 반환하자
    print("#{} {}".format(tc, result))