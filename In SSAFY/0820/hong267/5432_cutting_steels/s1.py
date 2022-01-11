import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    steels = input()

    cnt = 0
    current = 0
    for i in range(len(steels)):
        if steels[i] == '(':
            if steels[i+1] == ')': # cut 한다고 생각하고 현재 세로로 본 쇠막대기에 더해줌
                cnt += current
            else:
                current += 1 # '(' 다음 '('가 나오면 세로로 본 쇠막대기 증가
        else:
            if steels[i-1] == '(':
                pass
            else:
                current -= 1 # ')' 다음 ')'은 현재 세로로 본 쇠막대기 감소
                cnt += 1 # 감소되는 쇠막대기를 더해줌

    print('#{0} {1}'.format(tc, cnt))



