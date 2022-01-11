import sys
sys.stdin = open('input.txt')

def translator(s):
    stack = [] # 연산자와 피연산자 계산용
    result = []

    icp = {'(': 3, '+': 1, '*': 2} # 바깥
    isp = {'(': 0, '+': 1, '*': 2} # 안

    for i in s:

        if i.isdigit():
            result.append(i)

        elif i == ')':
            while stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()

        else:
            while stack and icp[i] <= isp[stack[-1]]:
                result.append(stack.pop())
            stack.append(i)

    while stack:
        result.append(stack.pop())

    return result

def caculator(s):
    stack = []

    for i in s:
        if i.isdigit():
            stack.append(int(i))

        elif i == '+':
            b = stack.pop()
            a = stack.pop()
            stack.append(a+b)

        elif i == '*':
            b = stack.pop()
            a = stack.pop()
            stack.append(a*b)

    answer = stack.pop()
    return answer

for tc in range(1, 11):
    n = int(input())
    s = input()

    s = translator(s)
    s = caculator(s)
    print('#{} {}'.format(tc, s))