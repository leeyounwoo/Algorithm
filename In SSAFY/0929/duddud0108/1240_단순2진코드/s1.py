import sys
sys.stdin = open('input.txt')
dict = {'0001101':0, '0011001':1, '0010011':2, '0111101':3, '0100011':4, '0110001':5, '0101111':6, '0111011':7, '0110111':8, '0001011':9}
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    code = [input() for _ in range(N)]

    for i in range(N):
        if '1' in code[i]:
            idx = code[i].rfind('1')
            secret = code[i][idx-55:idx+1]
            break

    num_list = []
    total = 0
    for i in range(0, 56, 7):
        num = dict[secret[i:i + 7]]
        if i % 2:
            total += num
        else:
            total += num*3
        num_list.append(num)

    if total % 10:
        answer = 0
    else:
        answer = sum(num_list)
    print('#{} {}'.format(tc, answer))
