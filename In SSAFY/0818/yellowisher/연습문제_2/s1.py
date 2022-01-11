
def is_empty():
    # 만약 스택의 길이가 0이라면, True
    if len(stack) == 0:
        return True
    return False

def check_matching(data):   # '((()))'

    for i in range(len(data)):  # 문자열 스캔
        if data[i] == '(':  # 스택에 push(왼쪽 괄호)
            stack.append(data[i])
        else:               # 스택에서 pop(오른쪽 괄호)
            # 만약 스택이 비어있는 경우
            if is_empty():
                return False
            stack.pop()

    if not is_empty():
        return False
    return True
stack = []
s1 = '()()((()))'
s2 = '((()((((()()((()())((())))))'
print(check_matching(s1))
print(check_matching(s2))