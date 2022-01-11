import sys
sys.stdin = open('input.txt')

def calculate(tokens):
    stack = []

    for token in tokens:
        if token == '+':
            stack.append(stack.pop() + stack.pop())
        elif token == '*':
            stack.append(stack.pop() * stack.pop())
        else:
            stack.append(int(token))
    return stack.pop()

for tc in range(1):
    N = int(input())
    string = input()
    flag = 0
    stack = []
    result = []

    for s in string:
        if s == '(':
            flag = 1
        elif s == '+':
            if flag == 0:
                while stack:
                    result.append(stack.pop())
            else:
                stack.append(s)
        elif s == '*':
            stack.append(s)
        elif s == ')':
            flag = 0
            while True:
                ans = stack.pop()
                if ans == '(':
                    ans = ''
                    break
                elif ans == ')':
                    ans = ''
                result.append(ans)
        else:
            result.append(s)

    while stack:
        result.append(stack.pop())

    # print("#{} {}".format(tc + 1, calculate(result)))
    print(result)