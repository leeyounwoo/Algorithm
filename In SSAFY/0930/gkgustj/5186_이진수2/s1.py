import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T+1):
    N = float(input())
    
    answer = ''
    while N:
        # 2를 곱한 정수 부분
        temp = int(N*2)
        answer += str(temp)
        N = N*2 - temp

        if len(answer) >= 13:
            answer = 'overflow'
            break
    
    print('#{} {}'.format(t, answer))