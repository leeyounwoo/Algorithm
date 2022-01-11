import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    formula = input().split()
    stack = []
    try:
        for i in formula:
            if i == '.':
                result = stack.pop()
                if len(stack) != 0:
                    result = 'error'
                break
            # 연산자를 만나면 스택의 숫자 두 개를 꺼내 연산하고 다시 넣기
            elif i == '+':
                stack.append(stack.pop(-2) + stack.pop())
            elif i == '-':
                stack.append(stack.pop(-2) - stack.pop())
            elif i == '*':
                stack.append(stack.pop(-2) * stack.pop())
            elif i == '/':
                stack.append(stack.pop(-2) // stack.pop())
            else:  # 숫자는 int형으로 변환
                stack.append(int(i))

    except:  # 에러
        result = 'error'

    print('#{} {}'.format(tc, result))