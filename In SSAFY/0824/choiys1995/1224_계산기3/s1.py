import sys
sys.stdin = open('input.txt')

isp = {'*': 2, '+': 1, '(': 0}
icp = {'*': 2, '+': 1, '(': 3}

T = 10

# 수식을 왼쪽에서 오른쪽으로 스캔하면서
# - 피연산자면 스택에 저장
# - 연산자면 필요한 수만큼의 피연산자를 스택에 꺼내서 연산을 실행하고 연산 결과를 다시 스택에 저장

for tc in range(1, T+1):
    N = int(input())
    string = input()
    postfix = [] # 후위 표기 스택
    calc = []  # 연산자 스택
    for i in string:
        if i.isdigit():  # .isdigit() = 문자열이 숫자로 구성되어있는지
            postfix.append(i)
        elif i == ')':
            # '(' 만날때 까지 postfix로 보내고 '(' 버림
            while postfix[-1] != '(':
                postfix.append(calc.pop())
            postfix.pop()
        else:
            # 스택안 연산자의 우선순위가 낮거나 같으면 pop해서 postfix로 보냄
            while calc and not icp[i] > isp[calc[-1]]:
                postfix.append(calc.pop())
            calc.append(i)
    while calc:  # 남은 연산자 postfix로
        postfix.append(calc.pop())

    # 계산
    stack = []
    for i in postfix:
        if i.isdigit():
            stack.append(int(i))
        elif i == '+':
            stack.append(stack.pop() + stack.pop())
        elif i == '*':
            stack.append(stack.pop() * stack.pop())

    # 결과
    print('#{} {}'.format(tc, stack[0]))