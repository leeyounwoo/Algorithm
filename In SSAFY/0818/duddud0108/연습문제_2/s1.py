import sys
sys.stdin = open('input.txt')

def is_empty(stack):
    if len(stack):
        return False
    else:
        return True

def check_bracket(data):
    stack = []
    for i in data:
        if i == '(':
            stack.append(i)
        else:
            if is_empty(stack):
                return False
            stack.pop()
    if is_empty(stack):
        return False
    return True

T = int(input())
for _ in range(T):
    brackets = input()
    print(check_bracket(brackets))

