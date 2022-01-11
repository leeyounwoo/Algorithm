def is_empty():
    # 만약 스택의 길이가 0이면 트루
    if len(stack) == 0:
        return True
    return False


def check_matching(data):

    for i in range(len(data)): # 문자열 스캔
        if data[i] == '(': # 스텍에서 푸쉬(왼쪽 괄호
            stack.append(data[i])
        else: # 스택에서 팝 (오른쪽 괄호)

            if is_empty():
                return False # 전체 짝 안맞음
            stack.pop()

    if not is_empty(): # 스택이 비어있지않다면 짝이 안맞음
        return False
    return True

stack = []
s1 = '((()((((()()((()())((())))))'
s2 = '()()((()))'
print(check_matching(s1))
print(check_matching(s2))

# 답이 왜다르지..