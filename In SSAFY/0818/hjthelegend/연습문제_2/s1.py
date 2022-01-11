def check(s):
    stack = []

    for i in s:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if stack:
                stack.pop()
            else:
                return False

    return len(stack) == 0

s1 = '( )( )((( )))'
s2 = '((( )((((( )( )((( )( ))((( ))))))'

print(check(s1))
print(check(s2))