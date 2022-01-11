def push(item):
    stack.append(item)


def pop():
    if len(stack) == 0:
        print('스택이 비어있습니다!')
        return
    return stack.pop()


def is_empty():
    if len(stack) == 0:
        return True
    return False


def check_matching(data):
    for brace in data:
        if brace == '(':
            push(brace)
        elif brace == ')':
            check = stack.pop()
            if check != '(':
                break
    else:
        if is_empty():
            return True
    return False


MAX_SIZE = 100
stack = []

s1 = '()()((()))'
s2 = '((()((((()()((()())((())))))'
result = check_matching(s1)
print(result)
result = check_matching(s2)
print(result)