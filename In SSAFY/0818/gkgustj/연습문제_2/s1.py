def check(string):
    stack = []

    for s in string:
        if s == '(':
            stack.append(s)
        elif s == ')':
            if stack:
                stack.pop()
            else:
                return False

    if stack:
        return False
    else:
        return True

str1 = '( )( )((( )))'
print(check(str1))

str2 = '((( )((((( )( )((( )( ))((( ))))))'
print(check(str2))

str3 = '()())'
print(check(str3))