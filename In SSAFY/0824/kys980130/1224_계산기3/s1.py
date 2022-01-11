import sys
sys.stdin = open("input.txt")

def isp(token):  # in-stack priority
    if token == '*':
        return 2
    if token == '+':
        return 1
    if token == '(':
        return 0


def icp(token):  # in-coming priority
    if token == '*':
        return 2
    if token == '+':
        return 1
    if token == '(':
        return 3


T = 10
for tc in range(1, T+1):
    N = int(input())
    string = input()
    stack = []
    cal = ''

    for char in string:
        if char.isdigit():
            cal += char
        elif char == ')':
            while stack:
                if isp(stack[-1]) < isp('('):
                    cal += stack.pop()
                elif stack[-1] == '(':
                    stack.pop()
        else:
            while stack:
                if icp(char) < isp(stack[-1]):
                    cal += stack.pop()
            stack.append(char)

    result = []
    for j in cal:
        if j == '+':
            num1 = int(result.pop())
            num2 = int(result.pop())
            result.append(num1+num2)
        elif j == '*':
            num1 = int(result.pop())
            num2 = int(result.pop())
            result.append(num1*num2)
        else:
            result.append(j)
    print('#{} {}'.format(tc, result.pop()))


