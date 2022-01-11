import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    N = float(input())
    # decimal -> binary

    # 소수점 아래 12자리 이내로 표현되는 이진수
    binary = []
    # 나누기 위한 값
    tmp = 1
    for _ in range(12):
        tmp *= 0.5
        if N - tmp >= 0:
            binary.append(1)
            N -= tmp #reset
            if not N:  # 숫자가 나누어 떨어지면 break
                break
        else :
            binary.append(0)

    # 12번 다 돌았는데 값이 있다면
    # 13자리 이상이 필요한 경우
    if N:
        result = 'overflow'
    else:
        result = ''
        for n in binary:
            result += str(n)

    print('#{} {}'.format(tc, result))