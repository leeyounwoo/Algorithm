string = '2+3*4/5'
stack = []

for i in range(len(string)):
    if string[i] in '0123456789':
        print(string[i], end='')
    elif string[i] in '+-*/':
        stack.append(string[i])
result = ''.join(stack[::-1])
print(result)

