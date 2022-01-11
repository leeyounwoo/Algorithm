stack = []
def isempty():
    if len(stack) == 0:
        return True
    else:
        return False

def check(string):
    stack = []
    for i in range(len(string)):
        if string[i] == '(':
            stack.append('(')
        elif string[i] == ')':
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    if len(stack) != 0:
        return False

    return True


a = '((( )((((( )( )((( )( ))((( ))))))'
print(check(a))
b = '( )( )((( )))'
print(check(b))