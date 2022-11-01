def solution(s):
    stack = []
    for word in s:
        if word == '(':
            stack.append(word)
        else:
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    if stack:
        return False

    return True