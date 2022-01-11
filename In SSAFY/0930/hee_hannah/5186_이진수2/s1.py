import sys
sys.stdin = open('input.txt')

t = int(input())
for tc in range(1, t+1):
    print('#{}'.format(tc), end=" ")
    n = float(input()) # 실수로 받아주고
    # 각 소숫점 아래의 자리수를 0.5로 나누자
    cnt = 1
    num = 0
    while n > 0:
        if n // (0.5**cnt) >= 1: # 0.5의 cnt 제곱으로 나누어진다면 0.5 0.25 0.125
            n = n % (0.5 ** cnt) # 나머지로 새로운 n을 만들고
            num += 10**(cnt-1) # 101 100등등 이진수를 만들기 위해 이렇게 0 1 2
            cnt += 1 # 자리수 더해주기
        elif n // (0.5**cnt) == 0: # 0이라면 나눌수없으니
            cnt += 1 # 자리수만
        if n == 0: # 다 나눳으면(나머지가 0이라면 새로운 n = 0)
            num = str(num) # 문자로 만들고
            print(num[::-1]) # 순서 뒤집기
            break
        if n == 0 and cnt > 12: # 12자리가 넘으면
            print('overflow') # 아웃
            break
        if cnt > 12 and n > 0: # 12자리가 넘으면
            print('overflow') # 아웃
            break

