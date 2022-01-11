import sys
sys.stdin = open('input.txt')

for T in range(1, 11):
    tc = int(input())
    code = list(map(int, input().split()))

    flag = False
    while True:
        if flag:
            break
        for i in range(1, 6):
            temp = code.pop(0)
            temp -= i
            if temp <= 0:
                temp = 0
                code.append(temp)
                flag = True
                break
            code.append(temp)

    print('#{}'.format(T), end=' ')

    for i in range(len(code)):
        print(code[i], end=' ')
    print()