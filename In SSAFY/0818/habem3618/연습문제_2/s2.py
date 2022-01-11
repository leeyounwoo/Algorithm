stack = []

def is_empty():
    # 만약 스택의 길이가 0이면 True
    if len(stack) == 0:
        return True
    return False

def check_matching(data):
    for i in range(len(data)):
        if data[i] == '(':
            stack.append(data[i])
        else:
            # 만약 스택이 비어있는 경우
            if is_empty():
                return False
            stack.pop()

    if not is_empty():
        return False
    return True
s1 = '( )( )((( )))'
s2 = '((( )((((( )( )((( )( ))((( ))))))'