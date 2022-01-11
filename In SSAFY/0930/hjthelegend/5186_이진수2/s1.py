import sys
sys.stdin = open('input.txt')

t = int(input())
# 0 초과 1 미만 십진수 N -> 이진수
# ex) 0.625 -> 0.101

# 출력 가능하면 0. 나머지 숫자 출력
# 13자리 이상인 경우 'overflow'

for tc in range(1, t+1):
    n = float(input())
    answer = ''

    cnt = -1
    while True:

        # 2**cnt # 1/2, 1/4, 1/8...
        # 나머지 더해주기
        answer += str(int(n // (2**cnt )))
        # n에 나머지를 남겨주기
        n %= (2**cnt)
        cnt -= 1

        # print(n)
        # print(answer)
        if n == 0 or cnt < -13: # 13자리 이상
            break

    if len(answer) == 13:
        answer = 'overflow'

    print('#{} {}'.format(tc, answer))