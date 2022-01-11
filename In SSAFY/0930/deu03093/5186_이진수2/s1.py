import sys
sys.stdin = open('input.txt')

for T in range(1, 1+int(input())):
    num = float(input())
    ans = ''
    temp = 0.5
    cnt = 0
    while num != 0:
        if num >= temp:
            num -= temp
            ans += '1'
        else:
            ans += '0'
        temp /= 2
        cnt += 1
        # 12자리가 됐을때 break
        if cnt == 12:
            break
    # while 문을 빠져나왔는데도 num이 0이 아니라면 overflow
    if num != 0:
        print('#{} {}'.format(T, 'overflow'))
    else:
        print('#{} {}'.format(T, ans))
