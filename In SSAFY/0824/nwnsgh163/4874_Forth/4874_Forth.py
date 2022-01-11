import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    n = input().split()
    lst = []
    try:
        for i in n:

            if i == '+':
                lst.append(lst.pop(-2) + lst.pop())
            elif i == '-':
                lst.append(lst.pop(-2) - lst.pop())
            elif i == '*':
                lst.append(lst.pop(-2) * lst.pop())
            elif i == '/':
                lst.append(lst.pop(-2) // lst.pop())
            elif i == '.':
                result = lst.pop()
                if len(lst) != 0:
                    result = 'error'
                break
            else:
                lst.append(int(i))

    except:
        result = 'error'

    print('#{} {}'.format(tc, result))

