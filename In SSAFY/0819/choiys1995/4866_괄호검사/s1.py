import sys
sys.stdin = open('input.txt')

T = int(input())

def check(data):
    for char in data:
        # 만약 열린괄호가 온다면 스택에 추가해줌
        if char == '(' or char == '{':
            stack.append(char)
        # 만약 닫힌 괄호가온다면
        elif char == ')' or char == '}':
            # 검사할 스택이 없다면 비어있는것!
            if not stack:
                return 0
            elif char == ')' and stack.pop() != '(':
                return 0
            elif char == '}' and stack.pop() != '{':
                return 0
    if stack:
        return 0
    return 1

for tc in range(1, T+1):
    data = list(input())
    stack = []
    print("#{} {}".format(tc, check(data)))