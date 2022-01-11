import sys
sys.stdin = open('input.txt')

t = int(input())
for tc in range(1, t+1):
    s = list(input().split())

    stack = []
    if len(stack) == 1:
        stack.append(11111111) # 디버깅
    result = 'error'

    try:
        for i in s:
            if i == '.':
                if len(stack) == 1:
                    result = stack.pop()
                else:
                    result = 'error'
                break
            elif i == '-':
                if len(stack) <= 1:
                    stack.append(1)
                    break
                b = stack.pop()
                a = stack.pop()
                stack.append(a-b)
            elif i == '+':
                if len(stack) <= 1:
                    stack.append(1)
                    break
                b = stack.pop()
                a = stack.pop()
                stack.append(a+b)
            elif i == '*':
                if len(stack) <= 1:
                    stack.append(1)
                    break
                b = stack.pop()
                a = stack.pop()
                stack.append(a*b)
            elif i == '/':
                if len(stack) <= 1:
                    stack.append(1)
                    break
                b = stack.pop()
                a = stack.pop()
                stack.append(a//b) # /로 할때는 케이스 5개만 정답..
            else:
                stack.append(int(i))
    except:
        result = 'error'

    print('#{} {}'.format(tc, result))