import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    # 괄호 인풋 받고
    parentheses = input()
    len_p = len(parentheses)
    steel = 0

    count = 0
    i = 0
    while i < len_p :
        if i+1 < len_p and parentheses[i] + parentheses[i+1] == '()':
            if steel :
                count += steel
            i += 2
        elif parentheses[i] == '(' :
            steel += 1
            i += 1
        elif parentheses[i] == ')' :
            steel -= 1
            i += 1
            count += 1
    print('#{} {}'.format(tc, count))



