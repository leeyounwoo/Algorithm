import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    string = list(map(str, input().split()))
    stack = []
    for i in range(len(string)):
        char = string[i]
        if char == '+':
            if len(stack) < 2: # 넣은 문자열이 0이나 1개라면
                print('#{} error'.format(tc)) # 에러출력
                break
            else:
                a = int(stack.pop()) # 빼내기
                b = int(stack.pop())
                stack.append(a + b) # 연산하고 다시 넣기
        elif char == '-':
            if len(stack) < 2:
                print('#{} error'.format(tc))
                break
            else:
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(a - b)
        elif char == '*':
            if len(stack) < 2:
                print('#{} error'.format(tc))
                break
            else:
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(a * b)
        elif char == '/':
            if len(stack) < 2:
                print('#{} error'.format(tc))
                break
            else:
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(a // b)
        elif char == '.': #종료하고 프린트
            print('#{} {}'.format(tc, *stack))
        else:
            stack.append(char) # 숫자들은 그냥 스택에 넣기


