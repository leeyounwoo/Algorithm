# ( )( )((( )))
# ((( )((((( )( )((( )( ))((( ))))))

arr = input()
stack = []

for i in arr:
    if i == '(':
        stack.append(i)

    elif i == ')':
        stack.pop()

if not stack:
    print('괄호의 짝이 맞습니다.')
else:
    print('괄호의 짝이 맞지 않습니다.')

