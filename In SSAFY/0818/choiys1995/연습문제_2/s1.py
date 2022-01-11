stack = []

def is_empty():
    if len(stack) == 0:
        return True
    return False

def check_matching(data):
    for i in range(len(data)):
        # '(' 이면 리스트에 넣어주기
        if data[i] == '(':
            stack.append(data[i])
        else:  # ')'
            if is_empty():
                return False
            stack.pop()

    if not is_empty():
        return False
    return True

s1 = '()()((()))'
s2 = '((()((((()()((()())((())))))'

print(check_matching(s1))
print(check_matching(s2))
