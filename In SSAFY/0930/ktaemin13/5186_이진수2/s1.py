import sys
sys.stdin = open('input.txt')


T = int(input())
for test_case in range(1, 1 + T):
    num = float(input())
    result = ''
    for i in range(1, 13):  # 탐색
        num *= 2
        result += str(int(num) % 2)  # 1의 자리
        if num % 1 == 0:  # 소수점
            break
    else:
        result = 'overflow'  # 12번 안에 break 되지 않을 경우 'overflow' 출력
    print('#{} {}'.format(test_case, result))
