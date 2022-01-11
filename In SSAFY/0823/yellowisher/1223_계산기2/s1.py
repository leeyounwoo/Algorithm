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

for tc in range(10):
    N = int(input())
    string = input()

    stack = []
    result = []

    for s in string:
        if s == '+':
            while stack:
                result.append(stack.pop())
            stack.append(s)
        elif s == '*':
            stack.append(s)
        else:
            result.append(s)

    while stack:
        result.append(stack.pop())

    print("#{} {}".format(tc + 1, calculate(result)))
